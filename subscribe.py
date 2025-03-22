import os
from google.cloud import pubsub_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vishnu-service-account.json.json"

subscriber = pubsub_v1.SubscriberClient()

subscriber_id = "projects/thermal-circle-453908-t8/subscriptions/topic-1-sub"
timeout = 5.0

def callback(message):
    print(message.data)
    message.ack()

future = subscriber.subscribe(subscriber_id, callback)

with subscriber:
    try:
        future.result(timeout=timeout)
    except TimeoutError:
        future.cancel()  # shutdown
        future.result()  # block until shutdown is complete
    
print("success")