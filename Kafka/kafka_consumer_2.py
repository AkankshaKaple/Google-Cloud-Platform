import pickle
from sklearn import *
import pandas as pd
import numpy as np
import os
from kafka import KafkaConsumer
from json import loads

consumer_1 = KafkaConsumer(
    'numtest_topic_1',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='my-group_1',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# consumer_2 = KafkaConsumer(
#     'numtest_topic_1',
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='latest',
#     enable_auto_commit=True,
#     group_id='my-group_2',
#     value_deserializer=lambda x: loads(x.decode('utf-8')))
#
model_path = "/home/administrator123/Akanksha/My_Work/GCP/Google-Cloud-Platform/Kafka/model/model.pickle"
output_file = '/home/administrator123/Akanksha/My_Work/GCP/Google-Cloud-Platform/Kafka/output.csv'

regressor = pickle.load(open(model_path, "rb"))

for message in consumer_1:
    df = pd.DataFrame([message.value])
    df.drop(columns=['Close','Volume'], inplace=True)
    prediction = regressor.predict(df)
    df['pred'] = prediction
    print("C_1")
    print(df)

# for message in consumer_2:
#     df = pd.DataFrame([message.value])
#     df.drop(columns=['Close','Volume'], inplace=True)
#     prediction = regressor.predict(df)
#     df['pred'] = prediction
#     print("C_2")
#     print(df)
