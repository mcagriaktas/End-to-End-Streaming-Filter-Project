#!/bin/bash

# WARNING
echo "YOUR CLASS NAME AND JAR FILE NAME MUST BE THE SAME!"

# Run the docker exec command with the constructed class name
docker exec -it spark-master /opt/spark/bin/spark-submit --class StreamingApp --master spark://172.80.0.110:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3,com.typesafe.play:play-json_2.12:2.9.4 /opt/submitfiles/main_2.12-0.1.0-SNAPSHOT.jar
