package config

// Kafka Brokers
var Hosts = []string{"localhost:9092", "localhost:9093", "localhost:9094"}

// Consuming Topic
var FromTopic = "rabbit.test"

// Consumer Group Name
var GroupName = "parsing-group"

// Consumer & Producer Number
var PartitionNum = 9

// Parser Num
var ParserNum = 18

// Producing Topic
var ToTopic = "rabbit.parsed"

// Sensor Field Key
var NameKey = "Name"
var IndexKey = "index"
var IdKey = "id"
var ServiceKey = "service"
var TimeKey = "timestamp"
var SiteKey = "site_id"
var FieldKey = "FieldDeviceLayer"
var HeaderKey = "header"

// Timestamp Format
var TimeFormat = "2006-01-02 15:04:05"

// 1024 * 1024 / 8 = 1 MiB Current 64KB
var MemKB = 1024 * 1024 / (8 * 16)
