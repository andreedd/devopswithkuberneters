import random
import string
import datetime
import threading


def output_logs():
    """Output random strings every 5s with timestamp"""
    letters = string.ascii_lowercase
    timestamp = datetime.datetime.now()
    threading.Timer(5.0, output_logs).start()
    print(f'timestamp: {timestamp} string: ' + ''.join(random.choice(letters) for i in range(20)))


if __name__ == "__main__":
    output_logs()