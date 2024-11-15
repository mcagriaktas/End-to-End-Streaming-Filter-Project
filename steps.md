### create a topic for raw:
./kafka-topics.sh --create --bootstrap-server localhost:9192 --topic raw --partitions 3 --replication-factor 3
./kafka-topics.sh --create --bootstrap-server localhost:9192 --topic low --partitions 3 --replication-factor 3
./kafka-topics.sh --create --bootstrap-server localhost:9192 --topic mid --partitions 3 --replication-factor 3
./kafka-topics.sh --create --bootstrap-server localhost:9192 --topic high --partitions 3 --replication-factor 3

### Schema registry:
curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
--data '{
  "schema": "{\"type\": \"record\", \"name\": \"Transaction\", \"fields\": [ {\"name\": \"id\", \"type\": \"string\"}, {\"name\": \"first_name\", \"type\": \"string\"}, {\"name\": \"last_name\", \"type\": \"string\"}, {\"name\": \"balance\", \"type\": \"double\"} ] }"
}' \
http://localhost:8081/subjects/raw-value/versions


curl http://localhost:8081/subjects/raw-value/versions

### Start producer.py:
python producer.py


### Scala start streaming:
spark-submit --class StreamingApp --master local[*] --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3,com.typesafe.play:play-json_2.12:2.9.4 target/scala-2.12/main_2.12-0.1.0-SNAPSHOT.jar





# Stop your containers
docker-compose down

# Start them again
docker-compose up -d

# Enter the Superset container
docker exec -it superset bash

# Upgrade the Superset database
superset db upgrade

# Create an admin user (if you haven't already)
superset fab create-admin \
    --username admin \
    --firstname Superset \
    --lastname Admin \
    --email admin@superset.com \
    --password admin

# Initialize Superset
superset init

# Exit the container
exit


After setup, access Superset UI:


Go to http://localhost:8088
Login with your admin credentials
Navigate to Data → Databases
Click "+ Database"
Add your Druid connection:

Database Name: druid
SQLAlchemy URI: druid://broker:8082/druid/v2/sql
Test the connection



If you need to debug connection issues:
docker exec -it superset curl broker:8082/druid/v2/sql -H "Content-Type: application/json" -d '{"query":"SELECT 1"}'


# Add PostgreSQL deep storage configuration
druid_storage_type=postgresql
druid_storage_connector_connectURI=jdbc:postgresql://postgres:5432/druid
druid_storage_connector_user=cagri
druid_storage_connector_password=35413541

# Update extensions to include PostgreSQL deep storage
druid_extensions_loadList=["druid-histogram", "druid-datasketches", "druid-lookups-cached-global", "postgresql-metadata-storage", "druid-multi-stage-query", "druid-kafka-indexing-service", "druid-postgresql-storage"]

# Configure segment storage
druid_segment_cache_locations=[{"path":"/opt/shared/segments","maxSize":10000000000}]


