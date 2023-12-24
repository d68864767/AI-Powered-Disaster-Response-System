```python
# Import necessary libraries
from google.cloud import vision
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import os
import json

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize Vision client
vision_client = vision.ImageAnnotatorClient()

# Initialize Natural Language client
language_client = language_v1.LanguageServiceClient()

def analyze_image(image_path):
    # Load the image from local storage
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform image analysis
    response = vision_client.annotate_image({
        'image': image,
        'features': [{'type_': vision.Feature.Type.LABEL_DETECTION}],
    })

    # Print out the results
    for annotation in response.label_annotations:
        print('Image contains {}: {:.2f}%'.format(annotation.description, annotation.score * 100))

def analyze_text(text):
    # Analyze sentiment of the text
    document = language_v1.types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT,
    )
    sentiment = language_client.analyze_sentiment(document=document).document_sentiment

    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

def run():
    # Replace with your own image paths and texts
    image_paths = ['path_to_your_image1.jpg', 'path_to_your_image2.jpg']
    texts = ['your_text1', 'your_text2']

    for image_path in image_paths:
        analyze_image(image_path)

    for text in texts:
        analyze_text(text)
```
