```python
# Import necessary libraries
from google.cloud import pubsub_v1
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import os
import json

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize Pub/Sub client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path('your_project_id', 'your_subscription_id')

# Initialize Natural Language client
client = language_v1.LanguageServiceClient()

def callback(message):
    print("Received message: {}".format(message))
    data = json.loads(message.data)

    # Analyze sentiment of the message
    document = language_v1.types.Document(
        content=data['text'],
        type=enums.Document.Type.PLAIN_TEXT,
    )
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

    message.ack()

def run():
    # Listen for messages on the subscription
    future = subscriber.subscribe(subscription_path, callback=callback)
    print("Listening for messages on {}...".format(subscription_path))

    # Keep the main thread alive
    try:
        future.result()
    except Exception as e:
        print("Listening for messages on {} threw an Exception: {}.".format(subscription_path, e))
        future.cancel()
```
