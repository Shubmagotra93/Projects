import requests

token = "1d65145a11886603427c5843c42b7a7f0d9962cdea7398fe0121eb0bbf3eb07c"
headers = {"Authorization": f"Bearer {token}"}

BASE_URL = "https://gorest.co.in/public/v2"
endpoint_POST = f"{BASE_URL}/users"
print(endpoint_POST)

payload = {"id": "11521","name":"Mr. Magotra","email":"magotra@mailinator.com","gender":"male","status":"active"}
response = requests.post(endpoint_POST, json= payload, headers=headers)
json_data = response.json()
print("POST API: ", json_data)
user_id = json_data.get('id')

####################################################################
# GET API
endpoint_GET = f"{BASE_URL}/users/{user_id}/"
print(endpoint_GET)
response_get = requests.get(endpoint_GET, headers= headers)
print("Get API: ", response_get.json())

####################################################################
# PATCH API
payload_patch = {"email":"shubhammagotra@mailinator.com"}

endpoint_PATCH = f"{BASE_URL}/users/{user_id}/"
print(endpoint_PATCH)
response_patch = requests.patch(endpoint_PATCH, json=payload_patch, headers=headers)
json_patch_data = response_patch.json()
print("PATCH API: ", json_patch_data)

####################################################################
# Delete API

endpoint_DELETE = f"{BASE_URL}/users/{user_id}/"
print(endpoint_DELETE)
response_patch = requests.delete(endpoint_DELETE, headers=headers)
json_delete_data = response_patch.json()
# print(response_patch.status_code)
# print("Delete API: ", json_delete_data.get('message'))
