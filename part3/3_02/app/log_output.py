#!/usr/bin/env python3

import random
import string
import requests
import os

from flask import Flask
app = Flask(__name__)

letters = string.ascii_lowercase


@app.route("/")
def home():
    return 'HELLO FLASK'


@app.route("/logs")
def request_logs():
    logs = output_logs()
    return f'logs: {logs}'


@app.route("/pingpong")
def pingpong():
    print('requesting http://pingpong-svc.log-app/pingpong')
    response = requests.get('http://pingpong-svc.log-app/pingpong')
    return response.content


def output_logs():
    """Output random string with timestamp"""
    try:
        with open('files/timestamp.txt', 'r') as f:
            timestamp = f.read()
        print('requesting http://pingpong-svc.log-app/pingpong')
        response = requests.get('http://pingpong-svc.log-app/pingpong')
        print(f'Response Content: {response.content}')
        pongs = response.content.decode("utf-8")
        logs = f'{os.getenv("MESSAGE")} {pongs}\n timestamp: {timestamp} string: ' + ''.join(random.choice(letters) for i in range(20))
    except FileNotFoundError:
        logs = 'No timestamps found'
    return logs


if __name__ == "__main__":
    output_logs()