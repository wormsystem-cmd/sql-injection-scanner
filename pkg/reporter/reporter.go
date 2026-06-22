package reporter

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/wormsystem-cmd/sql-injection-scanner/pkg/scanner"
)

type Report struct {
	ScanTime        time.Time         `json:"scan_time"`
	URL             string            `json:"url"`
	Vulnerabilities []scanner.ScanResult `json:"vulnerabilities"`
	Statistics      Statistics        `json:"statistics"`
}

type Statistics struct {
	TotalTests    int     `json:"total_tests"`
	Vulnerable    int     `json:"vulnerable"`
	Safe          int     `json:"safe"`
	Duration      float64 `json:"duration"`
}

func GenerateJSONReport(results []scanner.ScanResult, filename string) error {
	report := Report{
		ScanTime:        time.Now(),
		Vulnerabilities: results,
		Statistics: Statistics{
			TotalTests: len(results),
			Vulnerable: len(results),
		},
	}

	data, err := json.MarshalIndent(report, "", "  ")
	if err != nil {
		return err
	}

	return os.WriteFile(filename, data, 0644)
}

func GenerateCSVReport(results []scanner.ScanResult, filename string) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"URL", "Parameter", "Type", "Payload", "Confidence", "Response Time"})

	for _, result := range results {
		writer.Write([]string{
			result.URL,
			result.Parameter,
			result.Type,
			result.Payload,
			fmt.Sprintf("%.2f", result.Confidence),
			fmt.Sprintf("%dms", result.ResponseTime.Milliseconds()),
		})
	}

	return nil
}

func GenerateHTMLReport(results []scanner.ScanResult, filename string) error {
	htmlContent := `<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>SQL Injection Scanner Report</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            direction: rtl;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        .header {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
            text-align: center;
        }
        .header h1 { color: #333; margin-bottom: 10px; }
        .header p { color: #666; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-box {
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .stat-box h3 { color: #666; margin-bottom: 10px; }
        .stat-box .number { font-size: 32px; font-weight: bold; }
        .vulnerable { color: #e74c3c; }
        .safe { color: #27ae60; }
        .total { color: #3498db; }
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        th { background: #667eea; color: white; padding: 15px; text-align: right; }
        td { padding: 12px 15px; border-bottom: 1px solid #eee; }
        tr:hover { background: #f5f5f5; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ SQL Injection Scanner Report</h1>
            <p>Advanced SQL Injection Detection Tool | Powered by WORM SYSTEM</p>
            <p style="margin-top: 10px; font-size: 12px; color: #999;">©️ Copyright © 2024 WORM SYSTEM - All Rights Reserved</p>
        </div>
        <div class="stats">
            <div class="stat-box">
                <h3>إجمالي الاختبارات</h3>
                <div class="number total">` + fmt.Sprintf("%d", len(results)) + `</div>
            </div>
            <div class="stat-box">
                <h3>ثغرات مكتشفة</h3>
                <div class="number vulnerable">` + fmt.Sprintf("%d", len(results)) + `</div>
            </div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>الرابط</th>
                    <th>المعامل</th>
                    <th>نوع الثغرة</th>
                    <th>الحمولة</th>
                    <th>درجة الثقة</th>
                </tr>
            </thead>
            <tbody>
`

	for _, result := range results {
		htmlContent += fmt.Sprintf(`
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td><code>%s</code></td>
                    <td>%.0f%%</td>
                </tr>
`, result.URL, result.Parameter, result.Type, result.Payload, result.Confidence*100)
	}

	htmlContent += `
            </tbody>
        </table>
    </div>
</body>
</html>
`

	return os.WriteFile(filename, []byte(htmlContent), 0644)
}
