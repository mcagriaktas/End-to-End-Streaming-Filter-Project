# Handling Streaming Data with Apache Spark Reading with Druid and Dashboarding with Superset

| Software               | Description                    | Version   | UI-Ports                             |
|------------------------|--------------------------------|-----------|---------------------------------------|
| Superset               | Data visualization tool       |4.0.2     | 8088                                 |
| Druid Router           | Druid Router service          | 31.0.0    | 8888                                 |
| Druid Broker           | Druid Broker service          | 31.0.0    | 8082                                 |
| Druid Historical       | Druid Historical service      | 31.0.0    | 8083                                 |
| Druid Middle Manager   | Druid Middle Manager service  | 31.0.0    | 8091, 8100-8105                      |
| Druid Coordinator      | Druid Coordinator service     | 31.0.0    | 8081                                 |
| PostgreSQL             | Database service              | 16        | 5432                                 |
| Zookeeper              | Kafka coordination service    | 3.5.10    | 2181                                 |
| Spark Worker 2         | Spark worker node             | 3.5.3    | 58086                                |
| Spark Worker 1         | Spark worker node             | 3.5.3    | 58084                                |
| Spark Master           | Spark master node             | 3.5.3    | 4040, 7077, 5050, 58080              |
| Kafka Schema Registry  | Schema registry for Kafka     | Custom    | 18081                                |
| Kafka 3                | Kafka broker 3                | 3.8.0 KRaft    | 39092, 9192                                |
| Kafka 1                | Kafka broker 1                | 3.8.0 KRaft    | 19092, 9192                                |
| Kafka 2                | Kafka broker 2                | 3.8.0 KRaft    | 29092, 9192                                |
| Kafka UI               | Kafka user interface          | v0.7.2    | 18080                                |
