from flask import Flask, render_template, url_for
from requests_api import data_api

app = Flask(__name__)


@app.route('/')
def home():
    # return render_template('index.html', data=data_api)
    return data_api


if __name__ == "__main__":
    app.run(debug=True)

