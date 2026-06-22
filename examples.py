#!/usr/bin/env python3
# Examples - أمثلة الاستخدام

from scanner import SQLScanner
from detector import SQLDetector
import argparse

def example_basic():
    """مثال أساسي"""
    print("مثال 1: فحص بسيط")
    print("="*50)
    
    scanner = SQLScanner()
    args = argparse.Namespace(
        url='http://example.com/product?id=1',
        method='GET',
        params='id',
        advanced=False,
        output=None,
        verbose=True
    )
    scanner.run(args)

def example_post():
    """مثال مع POST"""
    print("\nمثال 2: فحص صفحة تسجيل دخول (POST)")
    print("="*50)
    
    scanner = SQLScanner()
    args = argparse.Namespace(
        url='http://example.com/login',
        method='POST',
        params='username,password',
        post_data='username=admin&password=test',
        advanced=True,
        output=None,
        verbose=True
    )
    scanner.run(args)

def example_advanced():
    """مثال متقدم"""
    print("\nمثال 3: فحص متقدم مع حفظ التقرير")
    print("="*50)
    
    scanner = SQLScanner()
    args = argparse.Namespace(
        url='http://example.com/search?q=test',
        method='GET',
        params='q',
        advanced=True,
        output='report',  # سيحفظ report.json و report.html
        verbose=True
    )
    scanner.run(args)

def example_detector():
    """مثال استخدام Detector مباشرة"""
    print("\nمثال 4: استخدام SQLDetector مباشرة")
    print("="*50)
    
    detector = SQLDetector(timeout=10)
    
    # فحص Error-based
    result = detector.test_error_based_injection(
        'http://example.com/product?id=1',
        'id'
    )
    
    print(f"النتيجة: {result}")
    
    # فحص Time-based
    result = detector.test_time_based_injection(
        'http://example.com/product?id=1',
        'id'
    )
    
    print(f"النتيجة: {result}")

def example_multiple_params():
    """مثال فحص عدة حقول"""
    print("\nمثال 5: فحص عدة حقول")
    print("="*50)
    
    scanner = SQLScanner()
    args = argparse.Namespace(
        url='http://example.com/search',
        method='POST',
        params='keyword,category,sort',
        post_data='keyword=test&category=1&sort=date',
        advanced=True,
        output='multi_report',
        verbose=True
    )
    scanner.run(args)

if __name__ == '__main__':
    print("SQL Injection Scanner - Examples\n")
    
    # قم بتشغيل الأمثلة التي تريدها
    # example_basic()
    # example_post()
    # example_advanced()
    # example_detector()
    # example_multiple_params()
    
    print("\nلتشغيل الأمثلة:")
    print("1. قم بتعديل الـ URLs في الأمثلة")
    print("2. قم بإلغاء التعليق عن الأمثلة التي تريد تشغيلها")
    print("3. قم بتشغيل: python examples.py")
