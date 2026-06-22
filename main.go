package main

import (
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli/v2"
	"github.com/wormsystem-cmd/sql-injection-scanner/cmd"
)

const (
	Version = "2.0.0"
	AppName = "SQL Injection Scanner"
)

func main() {
	app := &cli.App{
		Name:    AppName,
		Usage:   "Advanced SQL Injection Detection Tool",
		Version: Version,
		Author:  "WORM SYSTEM",
		Copyright: "©️ Copyright © 2024 WORM SYSTEM - All Rights Reserved",
		Description: `
Advanced SQL Injection Scanner built with Go for high performance

🛡️  Features:
  • Multi-threaded scanning
  • Advanced detection techniques
  • WAF bypass capabilities
  • Comprehensive reporting
  • Security-focused design

Produced by WORM SYSTEM - Enterprise Security Solutions
		`,
		Commands: []*cli.Command{
			{
				Name:  "scan",
				Usage: "فحص الموقع للثغرات",
				Action: cmd.ScanCommand,
				Flags: []cli.Flag{
					&cli.StringFlag{
						Name:  "url",
						Usage: "رابط الموقع المراد فحصه",
					},
					&cli.StringFlag{
						Name:  "urls-file",
						Usage: "ملف يحتوي على روابط متعددة",
					},
					&cli.StringFlag{
						Name:    "method",
						Value:   "GET",
						Usage:   "طريقة الفحص (GET, POST)",
					},
					&cli.StringFlag{
						Name:  "params",
						Usage: "الحقول المراد فحصها (مثال: id,name)",
					},
					&cli.StringFlag{
						Name:  "post-data",
						Usage: "بيانات POST",
					},
					&cli.StringSliceFlag{
						Name:  "headers",
						Usage: "رؤوس مخصصة",
					},
					&cli.StringFlag{
						Name:  "cookies",
						Usage: "Cookies مخصصة",
					},
					&cli.IntFlag{
						Name:    "timeout",
						Value:   10,
						Usage:   "مهلة انتظار الرد بالثواني",
					},
					&cli.IntFlag{
						Name:    "threads",
						Value:   5,
						Usage:   "عدد المعالجات المتزامنة",
					},
					&cli.BoolFlag{
						Name:  "advanced",
						Usage: "تفعيل الفحص المتقدم",
					},
					&cli.BoolFlag{
						Name:  "waf-bypass",
						Usage: "تفعيل تجاوز WAF",
					},
					&cli.StringFlag{
						Name:  "proxy",
						Usage: "استخدام وكيل",
					},
					&cli.StringFlag{
						Name:  "output",
						Usage: "حفظ التقرير في ملف",
					},
					&cli.StringFlag{
						Name:    "format",
						Value:   "json",
						Usage:   "صيغة التقرير (json, html, csv)",
					},
					&cli.BoolFlag{
						Name:  "verbose",
						Usage: "عرض التفاصيل الكاملة",
					},
					&cli.BoolFlag{
						Name:  "random-delays",
						Usage: "تأخيرات عشوائية بين الطلبات",
					},
					&cli.BoolFlag{
						Name:  "user-agent-rotation",
						Usage: "تغيير User-Agent",
					},
					&cli.BoolFlag{
						Name:    "verify-ssl",
						Value:   true,
						Usage:   "التحقق من شهادات SSL",
					},
				},
			},
		},
	}

	if err := app.Run(os.Args); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		log.Fatal(err)
	}
}
