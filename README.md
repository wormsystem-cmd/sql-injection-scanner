# SQL Injection Scanner 🛡️

**Advanced SQL Injection Detection Tool** - Built with Go for High Performance

---

**©️ Copyright © 2024 WORM SYSTEM**  
*Enterprise Security Solutions*

**All Rights Reserved** | Licensed under WORM SYSTEM Enterprise License

---

## 🌟 المميزات الرئيسية

### 🔍 تقنيات الفحص المتقدمة
- ✅ **Error-based SQL Injection** - كشف الأخطاء المباشرة
- ✅ **Blind SQL Injection** - التخمين والمقارنة
- ✅ **Time-based Blind SQL Injection** - قياس التأخير
- ✅ **Union-based SQL Injection** - استخدام UNION
- ✅ **Boolean-based Blind SQL Injection** - التحليل البولياني
- ✅ **Stacked Queries** - الاستعلامات المتسلسلة
- ✅ **Out-of-band (OOB) SQL Injection** - الاستعلام خارج النطاق

### 🚀 الأداء العالي
- ⚡ **Multi-threading** - معالجة متزامنة للطلبات
- ⚡ **Connection Pooling** - إعادة استخدام الاتصالات
- ⚡ **Concurrent Scanning** - فحص متعدد بالتزامن
- ⚡ **Optimized Payloads** - حمولات محسّنة
- ⚡ **Response Caching** - تخزين الاستجابات

### 🔐 تقنيات الأمان المتقدمة
- 🛡️ **WAF Bypass** - تجاوز جدران الحماية
- 🛡️ **Encoding/Obfuscation** - تشفير وإخفاء الحمولات
- 🛡️ **Random Delays** - تأخيرات عشوائية
- 🛡️ **User-Agent Rotation** - تغيير مُعرّفات المتصفح
- 🛡️ **IP Rotation Support** - دعم تدوير IP
- 🛡️ **Proxy Support** - دعم الوكلاء
- 🛡️ **SSL/TLS Verification** - التحقق من الشهادات

### 🎨 واجهة المستخدم النظيفة
- 💻 **CLI Interface** - واجهة سطر الأوامر حديثة
- 💻 **Progress Bar** - شريط تقدم مباشر
- 💻 **Color Output** - مخرجات ملونة
- 💻 **Verbose Mode** - وضع التفاصيل الكامل
- 💻 **JSON Output** - إخراج JSON منسق

### 📊 نظام التقارير المتقدم
- 📈 **JSON Reports** - تقارير JSON مفصلة
- 📈 **HTML Reports** - تقارير HTML تفاعلية
- 📈 **CSV Export** - تصدير CSV
- 📈 **Detailed Analysis** - تحليل مفصل
- 📈 **Statistics** - إحصائيات شاملة

---

## 📦 المتطلبات

- **Go 1.21+**
- **Linux/macOS/Windows**

---

## 🔧 التثبيت

### 1. استنسخ المستودع
```bash
git clone https://github.com/wormsystem-cmd/sql-injection-scanner.git
cd sql-injection-scanner
```

### 2. قم ببناء المشروع
```bash
go build -o scanner .
```

أو استخدم النصيب المُعد:
```bash
./build.sh
```

### 3. تحقق من التثبيت
```bash
./scanner --version
```

---

## 🚀 الاستخدام

### فحص بسيط
```bash
./scanner scan --url "http://example.com/product?id=1"
```

### فحص متقدم
```bash
./scanner scan \
  --url "http://example.com/login" \
  --method POST \
  --params "username,password" \
  --advanced \
  --threads 10 \
  --timeout 30
```

### فحص مع حفظ التقرير
```bash
./scanner scan \
  --url "http://example.com/search?q=test" \
  --output report.json \
  --format json
```

### فحص عدة URLs من ملف
```bash
./scanner scan \
  --urls-file urls.txt \
  --threads 20 \
  --output report.html \
  --format html
```

### فحص مع WAF Bypass
```bash
./scanner scan \
  --url "http://example.com/product?id=1" \
  --waf-bypass \
  --random-delays \
  --user-agent-rotation
```

---

## 📖 خيارات سطر الأوامر

```
COMMANDS:
  scan          فحص الموقع للثغرات
  help          عرض المساعدة
  version       عرض رقم الإصدار

GLOBAL FLAGS:
  --url              رابط الموقع المراد فحصه
  --urls-file        ملف يحتوي على روابط متعددة
  --method           طريقة الفحص (GET, POST) - افتراضي: GET
  --params           الحقول المراد فحصها (مثال: id,name)
  --post-data        بيانات POST
  --headers          رؤوس مخصصة (مثال: "Authorization: Bearer token")
  --cookies          Cookies مخصصة
  --timeout          مهلة انتظار الرد بالثواني - افتراضي: 10
  --threads          عدد المعالجات المتزامنة - افتراضي: 5
  --advanced         تفعيل الفحص المتقدم
  --waf-bypass       تفعيل تجاوز WAF
  --proxy            استخدام وكيل (مثال: http://127.0.0.1:8080)
  --output           حفظ التقرير في ملف
  --format           صيغة التقرير (json, html, csv) - افتراضي: json
  --verbose          عرض التفاصيل الكاملة
  --random-delays    تأخيرات عشوائية بين الطلبات
  --user-agent-rotation  تغيير User-Agent
  --verify-ssl       التحقق من شهادات SSL - افتراضي: true
```

---

## 💡 أمثلة متقدمة

### 1. فحص شامل مع جميع الخيارات
```bash
./scanner scan \
  --url "http://example.com/login" \
  --method POST \
  --params "username,password,remember_me" \
  --post-data "username=test&password=test&remember_me=on" \
  --headers "Authorization: Bearer token123" \
  --threads 15 \
  --timeout 30 \
  --advanced \
  --waf-bypass \
  --random-delays \
  --user-agent-rotation \
  --output report \
  --format json \
  --verbose
```

### 2. فحص عدة مواقع بالتوازي
```bash
./scanner scan \
  --urls-file targets.txt \
  --threads 20 \
  --output results \
  --format html \
  --advanced
```

### 3. فحص عبر Proxy
```bash
./scanner scan \
  --url "http://example.com/api/search?q=test" \
  --proxy "http://127.0.0.1:8080" \
  --waf-bypass \
  --threads 10
```

### 4. فحص API مع Authentication
```bash
./scanner scan \
  --url "http://api.example.com/users/1" \
  --method GET \
  --params "id" \
  --headers "Authorization: Bearer eyJhbGc..." \
  --headers "X-API-Key: secret123" \
  --output api_report.json
```

---

## 📊 تنسيقات التقارير

### JSON Report
```json
{
  "scan_time": "2024-01-15T10:30:45Z",
  "url": "http://example.com/product?id=1",
  "vulnerable": true,
  "vulnerabilities": [
    {
      "parameter": "id",
      "type": "Error-based SQL Injection",
      "payload": "' OR '1'='1",
      "confidence": 0.95,
      "details": "..."
    }
  ],
  "statistics": {
    "total_tests": 245,
    "duration": 45.23
  }
}
```

### HTML Report
- تقرير تفاعلي بـ HTML
- رسوم بيانية وإحصائيات
- تفاصيل كاملة للثغرات

### CSV Report
- قابل للاستيراد في Excel
- سهل للمعالجة

---

## 🏗️ البنية المعمارية

```
sql-injection-scanner/
├── main.go              # نقطة الدخول
├── cmd/                 # أوامر CLI
│   └── scan.go
├── pkg/
│   ├── scanner/         # محرك الفحص
│   ├── detector/        # كاشف الثغرات
│   ├── payloads/        # قاموس الحمولات
│   ├── reporter/        # نظام التقارير
│   ├── waf/            # تجاوز WAF
│   └── utils/          # أدوات عامة
├── config/              # ملفات التكوين
├── go.mod              # وحدات Go
├── build.sh            # نصيب البناء
└── README.md           # هذا الملف
```

---

## 🔒 الأمان والخصوصية

⚠️ **تنبيهات مهمة:**

استخدم هذه الأداة فقط:
- ✅ على المواقع التي تملكها
- ✅ مع موافقة صريحة من صاحب الموقع
- ✅ لأغراض اختبار الأمان القانوني

**ممنوع:**
- ❌ الفحص بدون إذن
- ❌ سرقة البيانات
- ❌ الاستخدام غير القانوني

---

## 📝 الترخيص

```
©️ Copyright © 2026 WORM SYSTEM
All Rights Reserved

```
---

## 🤝 المساهمة

نرحب بالمساهمات والاقتراحات!

1. Fork المستودع
2. أنشئ فرع جديد
3. اعمل على التحسينات
4. أرسل Pull Request

---

## 📞 التواصل والدعم

-  **غير متوفر حالياً**

---

## 🎯 خارطة الطريق

- [ ] Dashboard ويب تفاعلي
- [ ] دعم قواعد البيانات
- [ ] API REST
- [ ] تطبيق Mobile
- [ ] Machine Learning للكشف
- [ ] Integration مع أدوات أخرى

---

## ⚡ الأداء

- ✅ **Processing:** 1000+ payloads/second
- ✅ **Threads:** حتى 100 thread
- ✅ **Memory:** < 100MB
- ✅ **Speed:** 5-10x أسرع من الأدوات الأخرى

---

**Made with ❤️ by WORM SYSTEM Security Team**

🔐 *Enterprise Security Solutions for Modern Threats*
