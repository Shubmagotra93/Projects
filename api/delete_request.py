import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_delete_booking():
    booking_id = 1417  # Replace with an actual booking ID you want to update
    endpoint = f"{BASE_URL}/booking/{booking_id}"

    headers = {
        "Content-Type": "application/json",  # Specify the content type
        "Accept": "application/json",  # Specify the expected response format
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # Replace with valid credentials
    }
    response = requests.delete(endpoint, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    print(f"Response Headers: {response.headers}")
    # Optionally, you can also log JSON content if the response is in JSON format
    try:
        json_response = response.json()
        print(f"Response JSON: {json_response}")
    except ValueError:
        print("Response is not in JSON format.")
