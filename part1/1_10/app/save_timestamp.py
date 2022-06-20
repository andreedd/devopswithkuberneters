import datetime
import threading


def save_timestamp():
    """Saves timestamp to file every 5 seconds"""
    timestamp = datetime.datetime.now()
    threading.Timer(5.0, save_timestamp).start()
    with open('timestamp.txt', 'w') as f:
        print('saving timestamp...')
        f.write(f'timestamp: {timestamp}')


if __name__ == "__main__":
    save_timestamp()