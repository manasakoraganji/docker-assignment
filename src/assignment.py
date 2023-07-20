import pika
import sys
import time
import ssl
import os
import json
import datetime
from configparser import ConfigParser

config =ConfigParser(interpolation=None)
config.read("config/config.ini")
username = config["RMQ_Connection_Details"]["username"]
password = config["RMQ_Connection_Details"]["password"]
host = config["RMQ_Connection_Details"]["host"]
port = config["RMQ_Connection_Details"]["port"]
vhost = config["RMQ_Connection_Details"]["vhost"]

while True:
    print("*Connection Details*")
    print(username)
    print(password)
    print(host)
    print(port)
    print(vhost)
    time.sleep(10)