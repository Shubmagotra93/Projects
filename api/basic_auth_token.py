import requests
from requests.auth import HTTPBasicAuth

username = "admin"
password = "password123"

BASE_URL = "https://restful-booker.herokuapp.com"

# Authentication header (using HTTPBasicAuth)
auth = HTTPBasicAuth(username, password)

token_endpoint = f"{BASE_URL}/auth"

response = requests.post(token_endpoint, auth=auth)
if response.status_code == 200:
    token_data = response.json()
    token = token_data.get('token')
    print(f"Fetched Token: {token}")
else:
    print(f"Failed to fetch token. Status Code: {response.status_code}, Response: {response.text}")