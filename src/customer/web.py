import customer_cmd
import customer_create_app
import time
import logging
import json
from datetime import datetime, date, timedelta
from flask import Flask, jsonify,request,make_response

app = Flask(__name__)

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return str(obj)
    raise TypeError("Type %s not serializable" % type(obj))

@app.route('/customer/create',methods=['POST'])
def create():
    logging.info("request message : %s",request.json)

    cstr_cmd = customer_cmd.CustomerCommand(request.json['customerName'],request.json['address'],request.json['email'])
    response_data = {
        "service":"customer",
        "type":"create"
    }
    try:
        customer_id = customer_create_app.regist_customer(cstr_cmd)
        response_data["result"] = "true"
        response_data["customerId"] = customer_id
    except Exception as e:
        logging.error("system error : %s",e)
        response_data["result"] = "false"
        response_data["message"] = str(e)

    logging.info("response message : %s",response_data)
    return make_response(json.dumps(response_data, default=json_serial))


if __name__ == "__main__":
    formatter = '%(asctime)s : %(levelname)s : %(message)s'
    logging.basicConfig(level=logging.INFO, format=formatter)
    app.run(debug=False,host='0.0.0.0')