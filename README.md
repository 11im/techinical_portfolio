# Technical Portfolio
### Python, SQL, R, Java, Scala, Go, C/C++, Javascript 등 데이터 처리 언어 활용 능력
**[src.md](./src/src.md)** : Go 언어를 활용하여 Nested Json을 Parsing하여 작은 단위로 쪼개는 프로세스를 수행하고, Python을 활용하여 수집된 데이터를 추출하여 parquet로 압축합니다.
### Linux, Docker, Virtual Machines, Kubernetes 등을 활용한 데이터 활용 및 분석을 위한 환경 구축 여부
**[./yaml/docker.md](./yaml/docekr.md)** : linux 환경에서 Docker를 활용하여 전체 데이터 수집 인프라를 구축했습니다.
### Amazon AWS, Google GCP, MS Azure 등 클라우드 서비스 활용 능력
**[./aws/aws.md](./aws/aws.md)** : AWS 서비스를 활용하여 수집된 데이터를 분석했습니다.


</br>
</br>

# Abtract
이 프로젝트는 교내 마이크로 그리드의 센서 데이터를 서버에서 저장하는 파이프라인을 구축하기위한 파일럿 프로젝트 소스 코드입니다. 마이크로 그리드에서는 OPC UA를 활용하여 RabbitMQ를 통해 데이터를 외부로 전송합니다. 데이터는 Json 포맷으로 sample 디렉토리에 저장된 [sample.json](./sample/sample.json)과 같은 스키마입니다.
파이프라인은 다음과 같은 순서로 데이터를 InfluxDB에 저장합니다.

1. RabbitMQ의 Queue에 있는 데이터를 Kafka Connect에서 가져온다.
2. Kafka Connect에서 Apache Kafka의 Raw Json Topic에 저장한다.
3. Raw Json Topic의 Nested Json을 Parser에서 가공하여 Parsed Json Topic에 저장한다.
4. Telegraf가 Parsed Json Topic의 데이터를 읽어서 InfluxDB에 저장한다.

저장된 데이터는 장기간 보관을 위해 일정 기간이 지나면 Python Code를 통해 추출하여 Apache Parquet 형태로 압축합니다. 생성된 Parquet 파일은 AWS S3에 업로드 되며, AWS Glue를 통해 Parsing 되어 AWS Athena를 통해 SQL 쿼리합니다. 쿼리 결과는 다시 AWS S3에 csv 형태로 저장됩니다.

Parser는 Golang으로 구성되었으며, 추출 및 압축 코드는 Python(ipynb)로 구성했습니다. 또한 AWS 서비스는 AWS CLI를 활용했습니다.

</br>

# Requirements
1. Docker, Docker-compose
2. Python3, Python Libraries(./python/requirements.txt)
3. Golang
4. MakeFile

</br>

# Directories
1. yaml : docker-compose를 위한 yaml 파일들
2. config : docker 설정 파일들
3. plugin : Kafka Connect를 위한 Connect Plugin
4. src : 작성한 코드
    1. go-kafka-json-parser : golang 기반 json parser code
    2. python : 활용한 Python Script
5. aws : AWS 서비스들을 활용하기 위한 Bash Script
6. sample : sample.json
7. data : Apache Kafka와 InfluxDB의 데이터와 압축된 Parquet 파일 저장 경로


</br>

# 사용 Application, Version

| Description  | Value   |
|--------------|---------|
| InfluxDB     | 1.8   |
| Grafana      | 9.4.1   |
| Zookeeer     | confluent 7.2.1|
| Kafka     | confluent 7.4.0|
| Kafka Connect     | 7.3.3|
| Telegraf  | 1.26 |

</br>

# MakeFile
```make all``` : Telegraf를 제외한 모든 Docker Application 생성 </br>
```make topic``` : Kafka Topic 생성 </br>
```make telegraf``` : Telegraf 생성 </br>
```make telegraf``` : Telegraf 생성 </br>

# AWS
### AWS CLI 설치 후 Configure 해야함 </br>

```aws_cli.sh``` : AWS CLI 설치 </br>
```aws_auto_complete.sh``` : AWS CLI 자동 완성 설정 </br>
```s3.sh``` : AWS S3 Bucket 생성 및 Parquet Upload </br>
```glue.sh``` : AWS Glue 크롤러,DB 생성 </br>
```athena.sh``` : 질의 실행 및 쿼리 결과 다운로드 </br>