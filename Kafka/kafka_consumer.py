from kafka import KafkaConsumer
from json import loads
import pickle
from sklearn import *
import pandas as pd
import numpy as np
import os

consumer = KafkaConsumer(
    'numtest_topic_1',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

model_path = "/home/administrator123/Akanksha/My_Work/GCP/Google-Cloud-Platform/Kafka/model/model.pickle"
output_file = '/home/administrator123/Akanksha/My_Work/GCP/Google-Cloud-Platform/Kafka/output.csv'

regressor = pickle.load(open(model_path, "rb"))

for message in consumer:
    df = pd.DataFrame([message.value])
    print(df)
    df.drop(columns=['Close','Volume'], inplace=True)
    prediction = regressor.predict(df)
    df['pred'] = prediction

    os.path.exists(output_file)

    if os.path.exists(output_file):
        with open('output.csv', 'a') as f:
            df.to_csv(f, header=False)
    else:
        with open('output.csv', 'a') as f:
            df.to_csv(f, header=True)



