# Deployment Guide

This guide will walk you through the steps to deploy the AI-Powered Disaster Response System on Google Cloud.

## Prerequisites

- Google Cloud account with billing enabled
- Google Cloud SDK installed on your local machine
- Python 3.7 or later installed on your local machine
- Access to Google Cloud APIs (Pub/Sub, AI Platform, Vision API, Natural Language API, BigQuery, Datastore, and Maps API)

## Steps

1. **Set up your Google Cloud project**

   - Create a new project in the Google Cloud Console.
   - Enable the necessary APIs for your project (Pub/Sub, AI Platform, Vision API, Natural Language API, BigQuery, Datastore, and Maps API).
   - Create a service account for your project and download the JSON key file. This will be used to authenticate your application with Google Cloud.

2. **Prepare your application for deployment**

   - Clone the project repository to your local machine.
   - Replace the placeholder values in the code with your actual project ID, service account key file path, and other necessary details.
   - Install the necessary Python packages by running `pip install -r requirements.txt` in your project directory.

3. **Deploy your application to Google App Engine**

   - Navigate to your project directory in the terminal.
   - Initialize your App Engine application with the command `gcloud app create`.
   - Deploy your application with the command `gcloud app deploy`. This will upload your application to Google Cloud and start it.

4. **Verify the deployment**

   - Once the deployment is complete, you can view your application by navigating to `https://PROJECT_ID.REGION_ID.r.appspot.com` in your web browser (replace `PROJECT_ID` and `REGION_ID` with your actual project ID and region ID).
   - Test the different routes of your application to ensure that everything is working as expected.

## Notes

- The application uses Google Cloud Pub/Sub to ingest real-time data. You will need to set up a Pub/Sub topic and subscription, and publish messages to the topic for the application to process.
- The application uses Google Cloud BigQuery for data analysis. You will need to create a BigQuery dataset and table for the application to store and analyze data.
- The application uses Google Cloud Datastore for storing the processed data. You will need to create a Datastore kind for the application to store data.
- The application uses Google Cloud Vision API and Natural Language API for image and text analysis. You will need to ensure that these APIs are enabled and that your application has the necessary permissions to access them.
- The application uses Google Maps API for geospatial data visualization. You will need to ensure that this API is enabled and that your application has the necessary permissions to access it.

