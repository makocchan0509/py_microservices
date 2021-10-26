import mysql.connector
from mysql.connector import MySQLConnection
import os

def getMysqlConnection() -> MySQLConnection:

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
    print('Mysql connection status >-- ',conn.is_connected())

    return conn

if __name__ == '__main__':
    getMysqlConnection()