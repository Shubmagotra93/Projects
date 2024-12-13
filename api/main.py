import json

import requests

url = "http://216.10.245.166/Library/GetBook.php"
param = {"AuthorName": "Rahul Shetty"}

response = requests.get(url,params=param)
data_dict = response.json()
print(data_dict)
print("#"*30)
print(data_dict[0])
print("#"*30)
print(data_dict[1])
json.load()
json.loads()