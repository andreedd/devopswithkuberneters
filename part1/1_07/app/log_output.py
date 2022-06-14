import random
import string
import datetime
import threading

from flask import Flask
app = Flask(__name__)

letters = string.ascii_lowercase


@app.route("/")
def request_logs():
    logs = output_logs()
    return f'logs: {logs}'


def output_logs():
    """Output random strings with timestamp"""
    timestamp = datetime.datetime.now()
    logs = f'timestamp: {timestamp} string: ' + ''.join(random.choice(letters) for i in range(20))
    return logs


if __name__ == "__main__":
    output_logs()