import json

import requests


response = requests.get("https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=2")
print("status code: ",response.status_code)
# print(response.text)
# print(type(response.text))  # <class 'str'>
res = response.json()
# print(type(res))  # <class 'dict'>
# resp = json.loads(response.text)
# json_str = json.dumps(res, indent=4)
json_str = json.dump(res, )
print("json.dumps type :",type(json_str))
load = json.loads(json_str)
print("json.loads type: ", type(load))

# json.dumps() type : <class 'str'>
# json.loads() type:  <class 'dict'>
# json.dump() is used in Python to serialize a Python object\
# (e.g., dictionary or list) to a JSON-formatted string and write it directly to a file.


