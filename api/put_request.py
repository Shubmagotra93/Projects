import json

import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_update_booking():
    booking_id = 14078  # Replace with an actual booking ID you want to update
    endpoint = f"{BASE_URL}/booking/{booking_id}"

    with open("payload.json", 'r') as file:
        json_data = json.load(file)

# fetching payload and headers data from json file
    payload = json_data['update']
    header = json_data['headers']

    response = requests.put(endpoint, headers=header, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    print(f"Response Headers: {response.headers}")

