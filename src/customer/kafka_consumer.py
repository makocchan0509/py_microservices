from kafka import KafkaConsumer,TopicPartition
import os
import sys
import customer_verify_cmd
import customer_verify_app
import json
import logging

def main():

    logging.info('start consume')

    kafka_host_port = os.environ.get('KAFKA_HOSTPORT')
    kafka_consumer = os.environ.get('KAFKA_CONSUMER')

    # _consumer = KafkaConsumer(
    #     bootstrap_servers=[kafka_host_port],
    #     group_id="customer",
    #     consumer_timeout_ms=1000
    # )
    # tp = TopicPartition(kafka_consumer, 0)
    # _consumer.assign([tp])
    # _consumer.seek(tp, 25)
    # for message in _consumer:
    #     logging.info('topic: %s partition: %s offset: %s key: %s value: %s',message.topic,message.partition,message.offset,message.key,message.value.decode())

    consumer = KafkaConsumer(
        kafka_consumer,
        bootstrap_servers=[kafka_host_port],
        group_id="customer",
        auto_offset_reset='earliest'
    )
    try:
        while True:
            for message in consumer:
                try:
                    logging.info('topic: %s partition: %s offset: %s key: %s value: %s',message.topic,message.partition,message.offset,message.key,message.value.decode())
                    m_dict = json.loads(message.value.decode())
                    cmd = customer_verify_cmd.CustomerVerifyCmd(m_dict["customerId"],m_dict["orderId"])

                    customer_verify_app.verify_customer(cmd)
                    consumer.commit()
                    
                except Exception as e:
                    logging.error("system error : %s",e)
    except KeyboardInterrupt:
        logging.info('pressed Ctrl+C ... exit application')
        consumer.close(autocommit=False)
        sys.exit


if __name__ == '__main__':
    formatter = '%(asctime)s : %(levelname)s : %(message)s'
    logging.basicConfig(level=logging.INFO, format=formatter)
    main()

