# Filtering Streaming Data with Apache Spark Reading with Druid and Dashboarding with Superset

Hello everyone. In this project, I'll demonstrate how to filter streaming data using Apache Kafka. We'll store our raw data in a topic called raw_data, which contains data for 10,000 users and 1,000,000 processes. The raw data will be consumed and processed using three Kafka brokers.
During this process, we will retrieve the raw data with Scala Spark and filter it into three different topics:
- If the balance is less than 500, we'll produce it to the low topic.
- If the balance is between 500 and 2000, we'll produce it to the mid topic.
- For balances above 2000, we'll produce to the high topic.

Once the streaming starts, we will also read from the low, mid and high topics using Apache Druid. These three topics will be combined in Apache Druid. I will demonstrate how to create a new table in Druid, which can be queried using SQL. This is beneficial for data analytics teams, should they need it.
Additionally, we will create a streaming dashboard in Superset. Apache Druid plays a crucial role in this process, as it enables us to efficiently analyze and visualize the data.

## Artitecture

![image](https://github.com/user-attachments/assets/770e018e-756b-489b-b76b-7948f1749791)

## Software Versions
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
| Kafka Schema Registry  | Schema registry for Kafka     | 7.3.0    | 18081                                |
| Kafka 3                | Kafka broker 3                | 3.8.0 KRaft    | 39092, 9192                                |
| Kafka 1                | Kafka broker 1                | 3.8.0 KRaft    | 19092, 9192                                |
| Kafka 2                | Kafka broker 2                | 3.8.0 KRaft    | 29092, 9192                                |
| Kafka UI               | Kafka user interface          | v0.7.2    | 18080                                |

**Note**:
This is not a production environment, but you can follow these steps to configure and install it in your environment.

## Preparation steps
### Firstly, give full permission to the path:
```bash
sudo chmod 777 -R End-to-End-Streaming-Filter-Project
```

### Spark-submit run folder:
You can run your `JAR file` in the `containers/config/spark/submitfiles` directory.

### Datagenerator run folder:
You can run your `.py files` in the `datagenerator/json` directory.

### How to start the Containers and Project:
Just follow the article: https://medium.com/towardsdev/filtering-streaming-data-with-apache-spark-reading-with-druid-and-dashboarding-with-superset-3cc3fa936c79

