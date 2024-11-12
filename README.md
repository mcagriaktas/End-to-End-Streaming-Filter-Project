# Handling_Streaming_Data_with_Apache_Spark_Reading_with_Druid_and_Dashboarding_with_Superset

| Tool Name             | Description                     | Version | Ports                                                    |
|-----------------------|---------------------------------|---------|----------------------------------------------------------|
| Superset              | Data visualization tool         | 4.0.2   | 0.0.0.0:8088->8088/tcp                                   |
| Druid Router          | Query routing for Druid         | 31.0.0  | 0.0.0.0:8888->8888/tcp                                   |
| Druid Middle Manager  | Druid indexing service          | 31.0.0  | 0.0.0.0:8091->8091/tcp, 0.0.0.0:8100-8105->8100-8105/tcp |
| Druid Historical      | Druid historical data store     | 31.0.0  | 0.0.0.0:8083->8083/tcp                                   |
| Druid Broker          | Druid query broker              | 31.0.0  | 0.0.0.0:8082->8082/tcp                                   |
| Druid Coordinator     | Druid coordination service      | 31.0.0  | 0.0.0.0:8081->8081/tcp                                   |
| PostgreSQL            | Database for Druid              | 16      | 0.0.0.0:5432->5432/tcp                                   |
| Kafka UI              | Kafka topic management UI       | v0.7.2  | 0.0.0.0:18080->18080/tcp                                 |
| Zookeeper             | Kafka Zookeeper                 | 3.5.10  | 2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp, 8080/tcp     |
| Kafka Schema Registry | Schema registry for Kafka       | 7.3.0   | 0.0.0.0:18081->18081/tcp                                 |
| Kafka Broker 3        | Kafka broker                    | 3.8.0   | 0.0.0.0:39092->39092/tcp                                 |
| Kafka Broker 2        | Kafka broker                    | 3.8.0   | 0.0.0.0:29092->29092/tcp                                 |
| Kafka Broker 1        | Kafka broker                    | 3.8.0   | 0.0.0.0:19092->19092/tcp                                 |
