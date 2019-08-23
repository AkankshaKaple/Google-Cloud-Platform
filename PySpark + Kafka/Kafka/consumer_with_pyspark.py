#    Spark
from pyspark import SparkContext
#    Spark Streaming
from pyspark.streaming import StreamingContext
#    Kafka
from pyspark.streaming.kafka import KafkaUtils
#    json parsing
import json

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 5)

kafkaStream = KafkaUtils.createStream(ssc, 'cdh57-01-node-01.moffatt.me:2181'
                                      , 'spark-streaming-group-id', {'stockprice':1})

parsed = kafkaStream.map(lambda v: json.loads(v[1]))

parsed.count().map(lambda x:'Tweets in this batch: %s' % x).pprint()

ssc.start()
ssc.awaitTermination()