# Report Generator
# نظام إنشاء التقارير

import json
from datetime import datetime
from colorama import Fore, Style
from tabulate import tabulate

class Reporter:
    """فئة إنشاء التقارير"""
    
    def __init__(self):
        self.results = []
        self.start_time = datetime.now()
    
    def add_result(self, url, param, result):
        """إضافة نتيجة للتقرير"""
        self.results.append({
            'url': url,
            'parameter': param,
            'vulnerable': result.get('vulnerable', False),
            'type': result.get('type', 'N/A'),
            'payload': result.get('payload', 'N/A'),
            'timestamp': datetime.now().isoformat()
        })
    
    def generate_console_report(self):
        """إنشاء تقرير للشاشة"""
        print(f"\n{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}         SQL Injection Scanner - Report{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}\n")
        
        vulnerable_count = sum(1 for r in self.results if r['vulnerable'])
        total_count = len(self.results)
        
        print(f"{Fore.CYAN}Summary:{Style.RESET_ALL}")
        print(f"  Total Tests: {total_count}")
        print(f"  {Fore.GREEN}Safe: {total_count - vulnerable_count}{Style.RESET_ALL}")
        print(f"  {Fore.RED}Vulnerable: {vulnerable_count}{Style.RESET_ALL}\n")
        
        if self.results:
            table_data = []
            for result in self.results:
                status = f"{Fore.RED}✗ YES{Style.RESET_ALL}" if result['vulnerable'] else f"{Fore.GREEN}✓ NO{Style.RESET_ALL}"
                table_data.append([
                    result['url'],
                    result['parameter'],
                    status,
                    result['type']
                ])
            
            print(tabulate(table_data, headers=['URL', 'Parameter', 'Vulnerable', 'Type'], tablefmt='grid'))
        
        duration = (datetime.now() - self.start_time).total_seconds()
        print(f"\n{Fore.CYAN}Duration: {duration:.2f} seconds{Style.RESET_ALL}")
    
    def generate_json_report(self, filename='report.json'):
        """حفظ التقرير بصيغة JSON"""
        report = {
            'scan_time': self.start_time.isoformat(),
            'completed_time': datetime.now().isoformat(),
            'total_tests': len(self.results),
            'vulnerable_count': sum(1 for r in self.results if r['vulnerable']),
            'results': self.results
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"{Fore.GREEN}[+] تم حفظ التقرير: {filename}{Style.RESET_ALL}")
    
    def generate_html_report(self, filename='report.html'):
        """إنشاء تقرير HTML"""
        vulnerable_count = sum(1 for r in self.results if r['vulnerable'])
        total_count = len(self.results)
        safe_count = total_count - vulnerable_count
        
        html_content = f"""
<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>SQL Injection Scanner Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            direction: rtl;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background-color: #333;
            color: white;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
        }}
        .summary {{
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }}
        .summary-box {{
            flex: 1;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            color: white;
            font-weight: bold;
        }}
        .safe {{ background-color: #4CAF50; }}
        .vulnerable {{ background-color: #f44336; }}
        .total {{ background-color: #2196F3; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background-color: white;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: right;
        }}
        th {{
            background-color: #333;
            color: white;
        }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        .yes {{ color: #f44336; font-weight: bold; }}
        .no {{ color: #4CAF50; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>SQL Injection Scanner Report</h1>
        <p>تقرير فحص ثغرات SQL Injection</p>
        <p>الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="summary">
        <div class="summary-box total">
            <h3>عدد الاختبارات</h3>
            <h2>{total_count}</h2>
        </div>
        <div class="summary-box safe">
            <h3>آمنة</h3>
            <h2>{safe_count}</h2>
        </div>
        <div class="summary-box vulnerable">
            <h3>معرضة للخطر</h3>
            <h2>{vulnerable_count}</h2>
        </div>
    </div>
    
    <table>
        <tr>
            <th>الرابط</th>
            <th>الحقل</th>
            <th>معرضة للخطر</th>
            <th>نوع الثغرة</th>
            <th>الحمولة</th>
        </tr>
"""
        
        for result in self.results:
            vulnerable_text = '<span class="yes">نعم ✗</span>' if result['vulnerable'] else '<span class="no">لا ✓</span>'
            html_content += f"""
        <tr>
            <td>{result['url']}</td>
            <td>{result['parameter']}</td>
            <td>{vulnerable_text}</td>
            <td>{result['type']}</td>
            <td><code>{result['payload']}</code></td>
        </tr>
"""
        
        html_content += """
    </table>
</body>
</html>
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"{Fore.GREEN}[+] تم حفظ التقرير HTML: {filename}{Style.RESET_ALL}")
