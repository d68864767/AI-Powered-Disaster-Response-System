```python
# Import necessary libraries
from google.cloud import bigquery
import os
import json

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize BigQuery client
client = bigquery.Client()

def analyze_data(data):
    # Prepare the data for analysis
    rows_to_insert = [
        {u"disaster_type": data['disaster_type'], u"severity": data['severity'], u"location": data['location']},
    ]

    # Insert data into BigQuery
    errors = client.insert_rows_json('your_project_id.your_dataset_id.your_table_id', rows_to_insert)
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

    # Query the data
    query = """
        SELECT disaster_type, AVG(severity) as avg_severity, COUNT(*) as count
        FROM `your_project_id.your_dataset_id.your_table_id`
        GROUP BY disaster_type
        ORDER BY avg_severity DESC
    """
    query_job = client.query(query)

    # Print the results
    for row in query_job:
        print("Disaster type: {}, Average severity: {}, Count: {}".format(row.disaster_type, row.avg_severity, row.count))

def allocate_resources(data):
    # Based on the analysis, allocate resources
    if data['severity'] > 7:
        resources = {
            'emergency_personnel': 100,
            'aid': 1000
        }
    elif data['severity'] > 5:
        resources = {
            'emergency_personnel': 50,
            'aid': 500
        }
    else:
        resources = {
            'emergency_personnel': 10,
            'aid': 100
        }

    print("Allocated resources: {}".format(resources))

def run():
    # Replace with your own data
    data = {
        'disaster_type': 'earthquake',
        'severity': 8,
        'location': 'San Francisco'
    }

    analyze_data(data)
    allocate_resources(data)
```
