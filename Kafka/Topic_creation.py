from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

# Create topics
topic_list = [NewTopic(name="topic_1", num_partitions=1, replication_factor=1),
              NewTopic(name="topic_3", num_partitions=3, replication_factor=1)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)

# List all the topic present in a group
consumer = KafkaConsumer(group_id='test', bootstrap_servers=['localhost:9092'])
print(consumer.topics())

# Check number of partitions in a topic
print(consumer.partitions_for_topic('topic_3'))

print(consumer.subscription())
