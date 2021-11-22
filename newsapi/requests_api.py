from flask import Flask
import requests
import json

app = Flask(__name__)

response_data = requests.get('https://reqres.in/api/users?page=2')
data_api = response_data.json()
for d in data_api['data']:
    print(d)
# for data in response_data.json()['items']:
#     print(data['title'])