```python
# Import necessary libraries
from google.cloud import pubsub_v1
import os
import json

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize Pub/Sub client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('your_project_id', 'your_topic_id')

def send_notification(data):
    # Prepare the data for sending
    data = json.dumps(data).encode('utf-8')

    # Send the data
    future = publisher.publish(topic_path, data=data)
    print("Published message ID {}.".format(future.result()))

def run():
    # Replace with your own data
    data = {
        'disaster_type': 'earthquake',
        'severity': 8,
        'location': 'San Francisco',
        'emergency_personnel': 100,
        'aid': 1000
    }

    send_notification(data)
```
