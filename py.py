"""
This module provides functionality to login to an admin site and post data to an API endpoint.
"""

import requests
from requests.auth import HTTPBasicAuth

# Define the URLs
ADMIN_URL = "https://yousrowncastsite.com/admin/"
POST_URL = "https://yousrowncastsite.com/api/admin/config/video/streamoutputvariants"

# Define login credentials
USERNAME = "admin"
PASSWORD = "abc123"

# Start a session to persist the login
session = requests.Session()

# Send the GET request to the admin page with Basic Auth
admin_response = session.get(ADMIN_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))

# Check if login was successful
if admin_response.status_code == 200:
    print("Login successful")

    # Define the headers and the JSON data for the POST request
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }

    data = {
        "value": [
            {
                "framerate": 60,
                "videoPassthrough": False,
                "videoBitrate": 12000,
                "audioPassthrough": True,
                "audioBitrate": 0,
                "cpuUsageLevel": 2,
                "scaledHeight": None,
                "scaledWidth": None,
                "name": "4K"
            }
        ]
    }

    # Send the POST request with Basic Auth
    post_response = session.post(POST_URL, headers=headers, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))

    # Print the response
    print(f"Status Code: {post_response.status_code}")
    print(f"Response Text: {post_response.text}")
else:
    print("Login failed")

