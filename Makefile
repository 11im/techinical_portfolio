# Makefile

all: 
	docker-compose -f ./yaml/docker-compose.kafka.yml up -d
	docker-compose -f ./yaml/docker-compose.grafana.yml up -d
	docker-compose -f ./yaml/docker-compose.connect.yml up -d	
	docker-compose -f ./yaml/docker-compose.db.yml up -d
	docker-compose -f ./yaml/docker-compose.rabbit.yml up -d

db: 
	docker-compose -f ./yaml/docker-compose.db.yml up -d

grafana: 
	docker-compose -f ./yaml/docker-compose.grafana.yml up -d

kafka: 
	docker-compose -f ./yaml/docker-compose.kafka.yml up -d

rabbit: 
	docker-compose -f ./yaml/docker-compose.rabbit.yml up -d

connect: 
	docker-compose -f ./yaml/docker-compose.connect.yml up -d	

telegraf: 
	docker-compose -f ./yaml/docker-compose.telegraf.yml up -d

stop-telegraf: 
	docker-compose -f ./yaml/docker-compose.telegraf.yml down

stop-grafana: 
	docker-compose -f ./yaml/docker-compose.grafana.yml down

stop-kafka:
	docker-compose -f ./yaml/docker-compose.kafka.yml down
	
stop-rabbitmq: 
	docker-compose -f ./yaml/docker-compose.rabbit.yml down

stop-connect: 
	docker-compose -f ./yaml/docker-compose.connect.yml down

stop: 
	docker-compose -f ./yaml/docker-compose.kafka.yml down
	docker-compose -f ./yaml/docker-compose.grafana.yml down
	docker-compose -f ./yaml/docker-compose.rabbit.yml down
	docker-compose -f ./yaml/docker-compose.connect.yml down
	docker-compose -f ./yaml/docker-compose.db.yml down

topic:
	docker exec -it kafka_mq1 kafka-topics --bootstrap-server localhost:9092 --partitions 9 --replication-factor 3 --create --topic rabbit.raw
	docker exec -it kafka_mq1 kafka-topics --bootstrap-server localhost:9092 --partitions 9 --replication-factor 3 --create --topic rabbit.parsed
parser:
	cd ./src//go-kafka-json-parser; go mod tidy
	cd ./src/go-kafka-json-parser/cmd; go build -o parser && nohup ./parser -parser 15 -consumer 9 -producer 30 -fromTopic rabbit.raw > ../err.log &

connector:
	python3 ./python/connector.py

simulation:
	python3 ./python/rabbit.py