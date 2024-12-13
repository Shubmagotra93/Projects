import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_booking():
    endpoint = f"{BASE_URL}/booking/14078"
    response = requests.get(endpoint)
    print(f"Status Code: {response.status_code}")

    print(f"Response Body: {response.text}")
    # print(f"Response Headers: {response.headers}")
    # Optionally, you can also log JSON content if the response is in JSON format
    # try:
    #     json_response = response.json()
    #     print(f"Response JSON: {json_response}")
    # except ValueError:
    #     print("Response is not in JSON format.")
