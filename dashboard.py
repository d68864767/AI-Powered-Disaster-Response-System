```python
# Import necessary libraries
from google.cloud import bigquery
import os

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"

# Initialize BigQuery client
client = bigquery.Client()

def get_data():
    # Query the data
    query = """
        SELECT disaster_type, AVG(severity) as avg_severity, COUNT(*) as count
        FROM `your_project_id.your_dataset_id.your_table_id`
        GROUP BY disaster_type
        ORDER BY avg_severity DESC
    """
    query_job = client.query(query)

    # Prepare the data for the dashboard
    data = []
    for row in query_job:
        data.append({
            'disaster_type': row.disaster_type,
            'avg_severity': row.avg_severity,
            'count': row.count
        })

    return data
```
