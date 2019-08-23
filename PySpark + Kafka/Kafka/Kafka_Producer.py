# Program to create producer
from time import sleep
from json import *
import json
import requests as requests
from kafka import KafkaProducer
import requests
import os
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
# Serializer ==> Encoding

# Reading data directly
# for e in range(1000):
#     data = {'number' : e}
#     producer.send('numtest_topic', value=data)
#     sleep(5)


# Reading data from website
time = "5min"
symbol = "MSFT"
apikey = os.getenv('apikey')
label = "Time Series ({})".format(time)
topic = "stockprice"

link = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}&outputsize=full&apikey={}".format(symbol,time,apikey)
req = requests.get(link)

data = req.text

data = data.replace('1. open', 'Open').replace('2. high','High').replace('3. low', 'Low').replace('4. close', 'Close').replace('5. volume', 'Volume')

json_obj = json.loads(data)
dict_1 = json_obj[label]

for key in dict_1.keys():
    producer.send('numtest_topic_1', value=dict_1[key])
    sleep(5)
