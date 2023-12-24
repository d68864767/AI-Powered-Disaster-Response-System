# AI-Powered Disaster Response System

This project is an AI-powered disaster response system that utilizes Google Cloud's AI and machine learning capabilities to aid in disaster response efforts. The system analyzes various data sources to provide real-time insights during natural disasters, such as floods, wildfires, or earthquakes.

## Core Features

- Real-Time Data Analysis
- Disaster Impact Assessment
- Resource Allocation Recommendations
- User Interface for Emergency Responders
- Notification System

## Technologies

- Google Cloud Pub/Sub for data ingestion
- Google Cloud AI and Machine Learning APIs for data processing and analysis
- Google Cloud Vision API and Natural Language API for image and text analysis
- Google App Engine for hosting the application
- Google Maps API for geospatial data visualization

## Getting Started

### Prerequisites

- Python 3.7+
- Google Cloud Account
- Google Cloud SDK

### Installation

1. Clone the repo
   ```
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install the requirements
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set your Google Cloud credentials
   ```
   export GOOGLE_APPLICATION_CREDENTIALS="path_to_your_service_account_file.json"
   ```
2. Run the main script
   ```
   python main.py
   ```

## Project Structure

- `main.py`: The main script that runs the application.
- `data_analysis.py`: Contains the code for real-time data analysis.
- `image_text_analysis.py`: Contains the code for analyzing satellite and aerial imagery and processing news and social media content.
- `resource_allocation.py`: Contains the code for suggesting optimal resource allocation.
- `dashboard.py`: Contains the code for the dashboard that displays real-time insights and recommendations.
- `notification_system.py`: Contains the code for the system that sends alerts and updates.
- `app.yaml`: The App Engine configuration file.
- `index.html`, `style.css`, `script.js`: The frontend files for the dashboard.
- `requirements.txt`: The file listing the Python dependencies.
- `TESTING.md`: The file containing testing evidence.
- `DEPLOYMENT.md`: The file containing instructions for deploying the application on Google Cloud.

## Documentation

For more details, please refer to the [Documentation](https://github.com/your_username_/Project-Name/wiki)

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your_email@gmail.com

Project Link: [https://github.com/your_username_/Project-Name](https://github.com/your_username_/Project-Name)
