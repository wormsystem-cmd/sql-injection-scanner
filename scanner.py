#!/usr/bin/env python3
# SQL Injection Scanner
# أداة فحص ثغرات SQL Injection

import argparse
import sys
from urllib.parse import urlparse, parse_qs
from colorama import Fore, Style, init
from detector import SQLDetector
from reporter import Reporter

init(autoreset=True)

class SQLScanner:
    """فئة الماسح الرئيسية"""
    
    def __init__(self):
        self.detector = SQLDetector()
        self.reporter = Reporter()
    
    def scan_url(self, url, method='GET', params=None, advanced=False, data=None):
        """فحص رابط محدد"""
        try:
            # تحليل الرابط
            parsed_url = urlparse(url)
            
            # إذا لم يتم تحديد parameters، استخرجها من الرابط
            if not params:
                if method.upper() == 'GET':
                    query_params = parse_qs(parsed_url.query)
                    params = list(query_params.keys())
                elif data:
                    params = list(data.keys())
                else:
                    print(f"{Fore.RED}[-] لم يتم تحديد أي parameters{Style.RESET_ALL}")
                    return
            else:
                params = params.split(',')
            
            if not params:
                print(f"{Fore.RED}[-] لا توجد parameters للفحص{Style.RESET_ALL}")
                return
            
            # فحص كل parameter
            for param in params:
                param = param.strip()
                result = self.detector.scan(url, param, method, data, advanced)
                self.reporter.add_result(url, param, result)
                
                # طباعة النتيجة
                if result.get('vulnerable'):
                    print(f"{Fore.RED}[!] تم اكتشاف ثغرة!{Style.RESET_ALL}")
                    print(f"    النوع: {result['type']}")
                    print(f"    الحقل: {param}")
                    print(f"    الحمولة: {result['payload']}\n")
                else:
                    print(f"{Fore.GREEN}[✓] لا توجد ثغرة في {param}{Style.RESET_ALL}\n")
        
        except Exception as e:
            print(f"{Fore.RED}[-] خطأ: {e}{Style.RESET_ALL}")
    
    def run(self, args):
        """تشغيل الماسح"""
        print(f"{Fore.CYAN}")
        print("="*60)
        print("   SQL Injection Scanner 🛡️")
        print("="*60)
        print(f"{Style.RESET_ALL}")
        
        # تحضير البيانات
        data = None
        if args.method.upper() == 'POST' and args.post_data:
            # تحويل POST data
            data = {}
            for item in args.post_data.split('&'):
                if '=' in item:
                    key, value = item.split('=')
                    data[key.strip()] = value.strip()
        
        # فحص الرابط
        self.scan_url(
            args.url,
            method=args.method,
            params=args.params,
            advanced=args.advanced,
            data=data
        )
        
        # طباعة التقرير
        if args.verbose:
            self.reporter.generate_console_report()
        
        # حفظ التقرير
        if args.output:
            if args.output.endswith('.json'):
                self.reporter.generate_json_report(args.output)
            elif args.output.endswith('.html'):
                self.reporter.generate_html_report(args.output)
            else:
                self.reporter.generate_json_report(args.output + '.json')
                self.reporter.generate_html_report(args.output + '.html')
        else:
            self.reporter.generate_console_report()

def main():
    """الدالة الرئيسية"""
    parser = argparse.ArgumentParser(
        description='SQL Injection Scanner - أداة فحص ثغرات SQL Injection',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة الاستخدام:
  python scanner.py --url "http://example.com/product?id=1"
  python scanner.py --url "http://example.com/login" --method POST --params "username,password"
  python scanner.py --url "http://example.com/search?q=test" --advanced --output report.json
        """
    )
    
    parser.add_argument('--url', required=True, help='رابط الموقع المراد فحصه')
    parser.add_argument('--method', default='GET', choices=['GET', 'POST'], help='طريقة الفحص (GET أو POST)')
    parser.add_argument('--params', help='الحقول المراد فحصها (مثال: id,name,search)')
    parser.add_argument('--post-data', help='بيانات POST (مثال: username=admin&password=test)')
    parser.add_argument('--timeout', type=int, default=10, help='انتظار الرد بالثواني')
    parser.add_argument('--advanced', action='store_true', help='تفعيل الفحص المتقدم')
    parser.add_argument('--output', help='حفظ التقرير في ملف')
    parser.add_argument('--verbose', action='store_true', help='عرض التفاصيل الكاملة')
    
    args = parser.parse_args()
    
    try:
        scanner = SQLScanner()
        scanner.run(args)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] تم إيقاف الفحص من قبل المستخدم{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[-] خطأ غير متوقع: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == '__main__':
    main()
