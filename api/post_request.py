import json

import allure
import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_create_booking():
    endpoint = f"{BASE_URL}/booking"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    # here we load data from payload.json file
    with open("payload.json", 'r') as file:
        json_data = json.load(file)

    payload = json_data['create']

    response = requests.post(endpoint, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    # allure.attach(get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    print(f"Response Headers: {response.headers}")
