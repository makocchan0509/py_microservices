import json
import logging
import os
from typing import Dict
from kafka import KafkaProducer
from kafka.errors import KafkaError

logger = logging.getLogger(__name__)

def produce_message(message:str) -> None:

    kafka_host_port = os.environ.get('KAFKA_HOSTPORT')
    kafka_topic = os.environ.get('KAFKA_REPLY_TOPIC')
    
    producer = KafkaProducer(
        bootstrap_servers=[kafka_host_port],
        value_serializer=lambda m: json.dumps(m).encode('utf-8')
        )
    future = producer.send(kafka_topic,message)

    try:
        record_metadata = future.get(timeout=10)
        logger.info("Success send message topic: %s partition: %s offset: %s",record_metadata.topic,record_metadata.partition,record_metadata.offset)
    except KafkaError as e:
        # Decide what to do if produce request failed...
        logger.error("Failed send message :%s",e)
        raise Exception()
    finally:
        producer.close()




    