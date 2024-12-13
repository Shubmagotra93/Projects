import pytest
import requests
import csv

BASE_URL = "https://restful-booker.herokuapp.com"

def test_create_booking():
    endpoint = f"{BASE_URL}/booking"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    with open('payload.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)  # dictionary data
        #Convert row values to appropriate types and structure the payload
            payload = {
                "firstname": row['firstname'],
                "lastname": row['lastname'],
                "totalprice": int(row['totalprice']),
                "depositpaid": row['depositpaid'] == 'True',  # Convert to boolean
                "bookingdates": {
                    "checkin": row['checkin'],
                    "checkout": row['checkout']
                },
                "additionalneeds": row['additionalneeds']
            }
            response = requests.post(endpoint, headers=headers, json=payload)

            # Log the status code for debugging
            print(f"Status Code: {response.status_code}")

            assert response.status_code == 200, f"Expected status code 201, but got {response.status_code}"
