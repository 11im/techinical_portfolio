import requests

headers={"accept": "application/json"}
msg = {
       "name": "rabbitmq",
       "config": {
           "connector.class": "com.ibm.eventstreams.connect.rabbitmqsource.RabbitMQSourceConnector",
           "rabbitmq.username": "admin",
           "rabbitmq.password": "rabbitpassword",
           "acks": "1",
           "task.max": "3",
           "rabbitmq.queue": "test.queue",
           "bootstrap.servers": "kafka1:9092,kafka2:9092,kafka3:9092",
           "rabbitmq.virtual.host": "/",
           "rabbitmq.port": "5672",
           "rabbitmq.host": "localhost",
           "kafka.topic": "test.raw",
           "value.converter": "org.apache.kafka.connect.storage.StringConverter",
           "key.converter": "org.apache.kafka.connect.storage.StringConverter"
       }
   }
# Kafka Connect URL
url = "localhost:8083"

response = requests.post(url,headers=headers)
if response.status_code != 200 :
    print(response)