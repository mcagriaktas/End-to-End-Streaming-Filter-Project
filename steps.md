## Basic Steps:

### create a topic for raw:
```bash
./kafka-topics.sh --create --bootstrap-server localhost:9192 --topic raw --partitions 3 --replication-factor 3
./kafka-topics.sh --create --bootstrap-server localhost:9192 --topic low --partitions 3 --replication-factor 3
./kafka-topics.sh --create --bootstrap-server localhost:9192 --topic mid --partitions 3 --replication-factor 3
./kafka-topics.sh --create --bootstrap-server localhost:9192 --topic high --partitions 3 --replication-factor 3
```

```bash
### Schema registry:
curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
--data '{
  "schema": "{\"type\": \"record\", \"name\": \"Transaction\", \"fields\": [ {\"name\": \"id\", \"type\": \"string\"}, {\"name\": \"first_name\", \"type\": \"string\"}, {\"name\": \"last_name\", \"type\": \"string\"}, {\"name\": \"balance\", \"type\": \"double\"} ] }"
}' \
http://localhost:8081/subjects/raw-value/versions
```

### How to check schema
```bash
curl http://localhost:8081/subjects/raw-value/versions/1
```

### Start producer.py:
```bash
python producer.py
```

### Scala start streaming:
```bash
spark-submit --class StreamingApp --master local[*] --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3,com.typesafe.play:play-json_2.12:2.9.4 target/scala-2.12/main_2.12-0.1.0-SNAPSHOT.jar
```
