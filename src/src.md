# Source Code
[sample.json](../sample/sample.json)을 확인하면 불필요한 데이터가 많고 Nested 되어 있는 것을 확인할 수 있습니다. 이를 통째로 데이터베이스에 저장할 경우 한 row에 너무 많은 attribute로 인해 데이터베이스 저장, 조회 성능이 떨어집니다. 따라서 최소 단위로 데이터를 재구성 할 필요가 있습니다. golang으로 작성된 parser를 통해 불필요한 boolean, string 데이터는 제거하고 필요한 모니터링 데이터를 float 형태로 변환합니다. 또한 보다 하위 단위인 장비 유형 단위로 Json을 재구성하여 Kafka에 전송합니다. 하지만 시간이 지남에 따라 데이터가 너무 많아지면 InfluxDB의 성능이 자연스럽게 저하됩니다. 따라서 일정 기간이 지난 데이터는 추출하여 압축합니다. 압축한 데이터를 추후 AWS 서비스를 통해 분석합니다.

# Parser
[go-kafka-json-parser](./go-kafka-json-parser/) 디렉토리에 코드 구성되어 있습니다. [segmentio-kafka](https://github.com/segmentio/kafka-go) 라이브러리를 활용해서 Kafka Raw Json Topic에서 데이터를 읽어오고, [clarketm](github.com/clarketm/json) 라이브러리를 활용해 Json을 읽은 후 불필요한 attribute는 제거하고 하위 단위로 쪼갠 후 Marshal 합니다. 이후 다시 segmentio-kafka 라이브러리를 활용해 Kafka Parsed Json Topic에 전송합니다.

```make parser``` : Parser 빌드 및 실행 </br>

# Python
## Extract from InfluxDB
InfluxDB에 데이터가 일정 기간 이상 쌓으면 조회 성능이 감소합니다. 따라서 InfluxDB에 보관된 데이터를 일정 수준 이하로 유지하기위해, 또 보다 효율적인 디스크 활용을 위해 InfluxDB에서 데이터를 추출하여 Apache Parquet 형태로 압축합니다. [influx.ipynb](./python/influx.ipynb) 스크립트에 코드 작성되어 있습니다. [influxdb-python](https://github.com/influxdata/influxdb-python) 라이브러리를 통해 데이터를 추출하고 [pyarrow](https://arrow.apache.org/docs/python/index.html)를 통해 데이터를 [../data/compacted.gzip](../data/compacted.gzip/)에 장비 유형 단위로 파티셔닝하여 압축, 저장합니다. </br>
cli를 통해 csv로 데이터를 추출한 경우를 위해 [csv-to-parquet.ipynb](./python/csv-to-parquet.ipynb) 스크립트도 추가로 작성했습니다. 

## Simulation
파일럿 테스트를위해 더미 데이터를 생성하는 코드입니다. [sample.json](../sample/sample.json)과 동일한 데이터를 timestamp만 변경하며 RabbitMQ에 전송합니다. 추가로 Kafka Connect에 REST API를 통해 Connector를 생성합니다.

```make simulation``` : Simulation 시작 </br>
```make connector``` : RabbitMQ와 Kafka 연결 </br>
