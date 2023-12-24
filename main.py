```python
# Import necessary libraries
from flask import Flask, render_template
import data_analysis
import image_text_analysis
import resource_allocation
import dashboard
import notification_system

# Initialize Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze-data')
def analyze_data():
    data_analysis.run()
    return 'Data analysis complete.'

@app.route('/analyze-images-text')
def analyze_images_text():
    image_text_analysis.run()
    return 'Image and text analysis complete.'

@app.route('/allocate-resources')
def allocate_resources():
    resource_allocation.run()
    return 'Resource allocation complete.'

@app.route('/dashboard')
def show_dashboard():
    data = dashboard.get_data()
    return render_template('dashboard.html', data=data)

@app.route('/send-notifications')
def send_notifications():
    notification_system.run()
    return 'Notifications sent.'

# Run the app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
```
