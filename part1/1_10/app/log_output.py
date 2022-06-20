import random
import string

from flask import Flask
app = Flask(__name__)

letters = string.ascii_lowercase


@app.route("/")
def request_logs():
    logs = output_logs()
    return f'logs: {logs}'


def output_logs():
    """Output random string with timestamp"""
    try:
        with open('files/timestamp.txt', 'r') as f:
            timestamp = f.read()
        logs = f'timestamp: {timestamp} string: ' + ''.join(random.choice(letters) for i in range(20))
    except FileNotFoundError:
        logs = 'No timestamps found'
    return logs


if __name__ == "__main__":
    output_logs()