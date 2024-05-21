import requests
from requests.auth import HTTPBasicAuth

# Define the URLs
admin_url = "https://yousrowncastsite.com/admin/"
post_url = "https://yousrowncastsite.com/api/admin/config/video/streamoutputvariants"

# Define login credentials
username = "admin"
password = "abc123"

# Start a session to persist the login
session = requests.Session()

# Send the GET request to the admin page with Basic Auth
admin_response = session.get(admin_url, auth=HTTPBasicAuth(username, password))

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
    post_response = session.post(post_url, headers=headers, json=data, auth=HTTPBasicAuth(username, password))

    # Print the response
    print(f"Status Code: {post_response.status_code}")
    print(f"Response Text: {post_response.text}")
else:
    print("Login failed")
