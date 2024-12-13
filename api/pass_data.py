import json

import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_and_update_booking():
    create_endpoint = f"{BASE_URL}/booking"

    with open("payload.json", 'r') as file:
        create_payload = json.load(file)

    create_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    create_response = requests.post(create_endpoint, headers=create_headers, json=create_payload)

    assert create_response.status_code == 200, "Failed to create booking"
    booking_data = create_response.json()
    booking_id = booking_data.get("bookingid")
    print(f"Created Booking ID: {booking_id}")

    # --- Step 2: Update the Created Booking ---
    update_endpoint = f"{BASE_URL}/booking/{booking_id}"
    update_payload = {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-12-05",
            "checkout": "2024-12-15"
        },
        "additionalneeds": "Wi-Fi"
    }

    # Add Authorization Header for PUT request
    update_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # Replace with valid credentials
    }

    # Perform PUT request
    update_response = requests.put(update_endpoint, headers=update_headers, json=update_payload)

    # Validate PUT response
    assert update_response.status_code == 200, "Failed to update booking"
    updated_data = update_response.json()
    print(f"Updated Booking Data: {updated_data}")
