
import requests
import json

response_data = requests.get('http://127.0.0.1:5000')

print(response_data.json())
# data_api = response_data.json()
# print(data_api)
# for d in data_api['data']:
#     print(d)