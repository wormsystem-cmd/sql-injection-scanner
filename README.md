# SQL Injection Scanner 🛡️

أداة متقدمة لفحص ثغرات SQL Injection في المواقع والتطبيقات

## المميزات ✨

- ✅ فحص SQL Injection العادي (Normal)
- ✅ فحص Blind SQL Injection
- ✅ فحص Time-based SQL Injection
- ✅ دعم طلبات GET و POST
- ✅ تقارير تفصيلية
- ✅ حفظ النتائج في ملفات
- ✅ سهل الاستخدام

## التثبيت 📦

```bash
# استنساخ المستودع
git clone https://github.com/wormsystem-cmd/sql-injection-scanner.git
cd sql-injection-scanner

# تثبيت المتطلبات
pip install -r requirements.txt
```

## الاستخدام 🚀

### 1. فحص بسيط
```bash
python scanner.py --url "http://example.com/product?id=1"
```

### 2. فحص متقدم
```bash
python scanner.py --url "http://example.com/product?id=1" --method POST --advanced
```

### 3. فحص مع حفظ التقرير
```bash
python scanner.py --url "http://example.com/product?id=1" --output report.json
```

### 4. فحص عدة حقول
```bash
python scanner.py --url "http://example.com/login" --params "username,password" --method POST
```

## خيارات سطر الأوامر 📋

```
--url           : رابط الموقع المراد فحصه (مطلوب)
--method        : GET أو POST (افتراضي: GET)
--params        : الحقول المراد فحصها (مثال: id,name)
--timeout       : انتظار الرد بالثواني (افتراضي: 10)
--advanced      : تفعيل الفحص المتقدم
--output        : حفظ التقرير في ملف JSON
--verbose       : عرض التفاصيل الكاملة
```

## الأنواع المكتشفة 🔍

### 1. SQL Injection العادي
يكتشف الأخطاء المباشرة في الاستجابة

### 2. Blind SQL Injection
يستخدم تقنيات التخمين والمقارنة

### 3. Time-based SQL Injection
يقيس وقت الاستجابة للكشف عن الثغرة

### 4. Union-based SQL Injection
يستخدم جملة UNION للحصول على البيانات

## الملفات 📁

```
sql-injection-scanner/
├── scanner.py           # الملف الرئيسي
├── payloads.py          # قاموس الحمولات
├── detector.py          # محرك الكشف
├── reporter.py          # نظام التقارير
├── requirements.txt     # المتطلبات
├── examples.py          # أمثلة الاستخدام
└── README.md           # هذا الملف
```

## تحذيرات أمنية ⚠️

**استخدم هذه الأداة فقط:**
- ✅ على المواقع التي تملكها
- ✅ مع موافقة من صاحب الموقع
- ✅ لأغراض التطوير والاختبار

**ممنوع استخدامها:**
- ❌ على مواقع الآخرين بدون إذن
- ❌ لأغراض غير قانونية
- ❌ لسرقة البيانات

## أمثلة 📚

```python
from scanner import SQLScanner

# إنشاء كائن الماسح
scanner = SQLScanner()

# فحص رابط
result = scanner.scan("http://example.com/product?id=1")

# عرض النتائج
if result['vulnerable']:
    print("⚠️ الموقع عرضة للثغرة!")
    print(f"نوع الثغرة: {result['type']}")
    print(f"الحقل المتأثر: {result['parameter']}")
    print(f"الحمولة الناجحة: {result['payload']}")
else:
    print("✅ الموقع آمن")
```

## المساهمة 🤝

نرحب بمساهماتك! يمكنك:
- إضافة payloads جديدة
- تحسين الكشف
- إصلاح الأخطاء
- كتابة توثيق أفضل

## الترخيص 📄

MIT License

## التواصل 💬

إذا كان عندك أسئلة أو اقتراحات، تواصل معنا!

---

**تم إنشاؤه بـ ❤️ من قبل wormsystem-cmd**
