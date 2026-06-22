package waf

import (
	"encoding/hex"
	"fmt"
	"strings"
)

// Encoding techniques for WAF bypass

func EncodeHex(input string) string {
	return "0x" + hex.EncodeToString([]byte(input))
}

func EncodeURL(input string) string {
	replacer := strings.NewReplacer(
		" ", "%20",
		"'", "%27",
		"\"", "%22",
		"=", "%3D",
	)
	return replacer.Replace(input)
}

func EncodeDouble(input string) string {
	return EncodeURL(EncodeURL(input))
}

func EncodeUnicode(input string) string {
	var result string
	for _, char := range input {
		result += fmt.Sprintf("\\u%04x", char)
	}
	return result
}

func Obfuscate(payload string) []string {
	return []string{
		payload,
		EncodeHex(payload),
		EncodeURL(payload),
		EncodeDouble(payload),
		strings.ToUpper(payload),
		strings.ToLower(payload),
		strings.ReplaceAll(payload, " ", "/**/ "),
		strings.ReplaceAll(payload, " ", "+"),
	}
}
