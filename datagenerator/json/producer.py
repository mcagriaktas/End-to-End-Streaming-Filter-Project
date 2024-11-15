import json
import time
from confluent_kafka import Producer

KAFKA_TOPIC = 'raw'
KAFKA_BROKERS = 'localhost:19092,localhost:29092,kafka3:39092' 

producer_conf = {
    'bootstrap.servers': KAFKA_BROKERS,
    'linger.ms': 10,
    'enable.idempotence': True 
}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    """ Called once for each message to confirm delivery to Kafka """
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record produced to {msg.topic()} partition [{msg.partition()}] @ offset {msg.offset()}")

with open("shuffled_bank_dataset.json", "r") as f:
    data = json.load(f)

limit = 1000000

for i, record in enumerate(data):
    if i >= limit:
        break
    try:
        producer.produce(
            KAFKA_TOPIC,
            key=str(record["id"]), 
            value=json.dumps(record),
            callback=delivery_report 
        )
        producer.poll(0.01)
        #time.sleep(0.5)
    except Exception as e:
        print(f"Failed to produce record: {e}")

producer.flush()

print("Finished producing first 10,000 messages.")
