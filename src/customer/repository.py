import customer
import mysql.connector
from mysql.connector import MySQLConnection
from typing import Tuple
import time
import logging
import os

logger = logging.getLogger(__name__)

def save(entity:customer, conn:MySQLConnection):

    cursor = conn.cursor()
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')

    query = "INSERT INTO customer_table(customer_id,customer_name,address,email,create_date,update_date) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(entity.customer_id,entity.customer_name,entity.address,entity.email,time_stamp,time_stamp))

    cursor.close()

def find_by_id(customer_id:str) -> Tuple:
    conn = getConnection()
    cursor = conn.cursor()
    query = "SELECT customer_id,customer_name,address,email,create_date,update_date FROM customer_table WHERE customer_id = %s"
    cursor.execute(query,(customer_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return result

def getConnection() -> MySQLConnection:

    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_port = os.environ.get('MYSQL_PORT')
    mysql_user = os.environ.get('MYSQL_USER')
    mysql_pass = os.environ.get('MYSQL_PASSWORD')
    mysql_db = os.environ.get('MYSQL_DATABASE')

    conn = mysql.connector.connect(
        host = mysql_host,
        port = mysql_port,
        user = mysql_user,
        password = mysql_pass,
        database = mysql_db
    )

    conn.ping(reconnect = True)
    if not conn.is_connected():
        raise Exception('can not connect to DB!!')

    return conn

if __name__ == "__main__":
    conn = getConnection()
    entity = customer.Customer("masem","xxxxx","xxx@xxx.com")

    save(entity,conn)

    conn.commit()
    conn.close()

