from google.cloud import pubsub_v1
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vishnu-service-account.json.json"

publisher = pubsub_v1.PublisherClient()
topic = "projects/thermal-circle-453908-t8/topics/topic-1"

message = 'Hi Welcome to Russia'

future = publisher.publish(topic, message.encode('utf-8'))
future.result()

print("message sent")


