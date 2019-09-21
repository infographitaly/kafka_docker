#Grab KafkaProducer from Kafka Python library
import os
import json
from time import sleep
from kafka import KafkaProducer
import socket
#from transactions import create_random_transaction

#import logging
#logging.basicConfig(level=logging.DEBUG)


#grab the URL del broker (from an environment variable). 
#Producers use that URL to bootstrap their connection to the Kafka cluster
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
print("*"*30)
print(KAFKA_BROKER_URL)
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
TRANSACTIONS_PER_SECOND = float(os.environ.get('TRANSACTIONS_PER_SECOND'))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND


ip = '172.21.0.16'
port = 6900

if __name__ == '__main__':
    print("*"*30)
    print(KAFKA_BROKER_URL)
    producer = KafkaProducer(
        bootstrap_servers= KAFKA_BROKER_URL, #KAFKA_BROKER_URL,
        #Encode all values as JSON
        value_serializer = lambda value: json.dumps(value).encode(),
        api_version=(0, 10, 2)
    )
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((ip, port))
    while True:
        data, addr = sock.recvfrom(1024)
        data_conv = json.loads(data)
        #transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value = data_conv)
        #DEBUG
        print(data_conv)
        #sleep(SLEEP_TIME)

"""
# Define the port on which you want to connect
ip = '172.21.0.16'
#ip = '172.21.0.3'
#port = 58793
port = 6900

import socket
import json

#UDP_IP = "127.0.0.1"
#UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((ip, port))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data_conv = json.loads(data)
    print(type(data_conv),data_conv)

"""