import customer_verify_cmd
import logging
import repository
import json
import kafka_producer

logger = logging.getLogger(__name__)

def verify_customer(cmd:customer_verify_cmd):

        result = repository.find_by_id(cmd.customer_id)
        message = {
            "service":"customer",
            "type":"verify",
            "orderId":cmd.order_id,
            "customerId": cmd.customer_id,
        }
        
        if result is None:
            logger.error("Customer not found: %s",cmd.customer_id)
            message["result"] = "false"
            message["message"] = "customer not found"
        else:
            message["result"] = "true"
        
        print(json.dumps(message,ensure_ascii=False))
        kafka_producer.produce_message(message)


