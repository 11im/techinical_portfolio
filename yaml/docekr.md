# Docker
프로젝트 환경을 빠르게 구축하고 배포/이관하기 위해 Docker를 통해 어플리케이션들을 실행시킵니다. 보다 쉽고 명확한 자원 관리와 버전 관리를 위해 docker-compose를 활용했습니다. 또한 [MakeFile](../Makefile)을 활용해 더욱 명령어를 간소화했습니다.

# 사용 Application, Version

| Description  | Value   | Port |
|--------------|---------|------|
| InfluxDB     | 1.8   | 8086 |
| Grafana      | 9.4.1   | 3000 |
| Zookeeer     | confluent 7.2.1| 2181 ~ 2183|
| Kafka     | confluent 7.4.0| 9092 ~ 9094|
| Kafka Connect     | 7.3.3| 8083 |
| Telegraf  | 1.26 | - |
| RabbitMQ  | 3.10.7 | 5672, 15672 |

# 어플리케이션 상세
1. InfluxDB : 시계열 특화 데이터베이스로 최근 데이터를 저장합니다. [docker-compose.db.yml](./docker-compose.db.yml)에 환경이 정의 되어 있습니다.
2. Grafana : 대시보드 및 시각화 생성을 위한 어플리케이션입니다. InfluxDB 및 다양한 데이터 소스와의 호환성이 좋아 도입했습니다. [docker-compose.grafana.yml](./docker-compose.grafana.yml)에 환경이 정의 되어 있습니다.
3. Zookeeper : Apache Kafka를 활용하기 위한 오케스트레이션 어플리케이션입니다. 3개 노드로 구성되며 [docker-compose.kafka.yml](./docker-compose.kafka.yml)에 Kafka와 함께 정의 되어 있습니다.
4. Kafka : 실시간 메세지 플랫폼입니다. 3개의 브로커로 구성되어 있으며, Zookeeper에 의존성이 있습니다. 추후 확장성을 위해 도입했습니다. [docker-compose.kafka.yml](./docker-compose.kafka.yml)에 Zookeeper와 함께 정의 되어 있습니다.
5. Kafka Connect : 데이터 소스로부터 데이터를 가져와 Kafka에 전송하는 역할을 합니다. Rest API를 통해 데이터 소스로부터의 연결을 자동화하기위해 도입했습니다. Kafka에 의존성이 있습니다. [docker-compose.kafka.yml](./docker-compose.kafka.yml)에 Kafka와 함께 정의 되어 있습니다
6. Telegraf : Kafka로부터 데이터를 읽어 InfluxDB에 주입하는 역할을 합니다. 활용성이 좋고 가벼우며, InfluxDB와 호환성이 좋아 도입했습니다. [docker-compose.telegraf.yml](./docker-compose.telegraf.yml)에 정의되어 있습니다. 
7. RabbitMQ : 실제 프로젝트에는 외부의 RabbitMQ에서 데이터를 가져오지만, 파일럿 테스트를 위해 로컬에 RabbitMQ를 띄워 활용합니다. [docker-compose.rabbit.yml](./docker-compose.rabbit.yml)에 정의되어 있습니다.

# Makefile
전체 구축 과정 및 시뮬레이션 자동화를 위해 MakeFile을 활용했습니다. 명령어는 다음과 같습니다.

```make all``` : Telegraf를 제외한 모든 Docker Application 생성 </br>
```make topic``` : Kafka Topic 생성 </br>
```make telegraf``` : Telegraf 생성 </br>
```make telegraf``` : Telegraf 생성 </br>
```make connector``` : RabbitMQ와 Kafka 연결 </br>
```make parser``` : Parser 빌드 및 실행 </br>
```make simulation``` : Simulation 시작 </br>