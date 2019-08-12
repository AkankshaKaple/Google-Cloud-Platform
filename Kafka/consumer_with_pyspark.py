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
                                      , 'spark-streaming-group-id', {'twitter':1})

parsed = kafkaStream.map(lambda v: json.loads(v[1]))

parsed.count().map(lambda x:'Tweets in this batch: %s' % x).pprint()

authors_dstream = parsed.map(lambda tweet: tweet['user']['screen_name'])

author_counts = authors_dstream.countByValue()
author_counts.pprint()

author_counts_sorted_dstream = author_counts.transform(\
  (lambda foo:foo\
   .sortBy(lambda x:( -x[1]))))
author_counts_sorted_dstream.pprint()
