from flask import Flask, render_template
from requests_data import response_data

import json


print(response_data.json())

data = response_data.json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)

