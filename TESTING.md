# TESTING.md

This document provides a guide on how to test the AI-Powered Disaster Response System.

## Testing Environment

Ensure that you have the following:

- Python 3.7 or later installed.
- Google Cloud SDK installed.
- Access to Google Cloud Console with necessary permissions.
- All the necessary libraries installed as listed in `requirements.txt`.

## Testing Steps

### 1. Unit Testing

Each module (`data_analysis.py`, `image_text_analysis.py`, `resource_allocation.py`, `dashboard.py`, `notification_system.py`) should be tested individually to ensure they function as expected.

#### Data Analysis Module

Run the `data_analysis.py` script and verify that it's able to ingest data from Pub/Sub and analyze it using the Natural Language API.

```bash
python data_analysis.py
```

#### Image and Text Analysis Module

Test the `image_text_analysis.py` script with different images and text inputs to ensure it's able to analyze them correctly.

```bash
python image_text_analysis.py
```

#### Resource Allocation Module

Test the `resource_allocation.py` script to ensure it's able to analyze data and suggest optimal resource allocation.

```bash
python resource_allocation.py
```

#### Dashboard Module

Run the `dashboard.py` script and verify that it's able to fetch data from BigQuery and return it in the expected format.

```bash
python dashboard.py
```

#### Notification System Module

Test the `notification_system.py` script to ensure it's able to send notifications correctly.

```bash
python notification_system.py
```

### 2. Integration Testing

After unit testing, the entire system should be tested together. Run the `main.py` script and verify that all routes are working as expected.

```bash
python main.py
```

Visit `http://127.0.0.1:8080/` in your browser and navigate through the different routes to ensure they're functioning correctly.

### 3. Load Testing

To test the system's ability to handle high volumes of data and scale during peak usage, you can use load testing tools like Apache JMeter or Locust.

### 4. User Interface Testing

Ensure that the dashboard is user-friendly and accessible. Check the visualization of data and ensure that it's easy to understand.

### 5. Notification System Testing

Verify that the notification system is able to send alerts and updates to the correct recipients and that the alerts contain the correct information.

## Reporting Issues

If you encounter any issues while testing, please document them with the following information:

- Description of the issue.
- Steps to reproduce the issue.
- Expected result.
- Actual result.

This will help in troubleshooting and fixing the issue.
