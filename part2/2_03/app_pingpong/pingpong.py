from multiprocessing import Value
from unicodedata import name

counter = Value('i', 0)

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return f'Hello pingpong'


@app.route('/pingpong')
def count():
    with counter.get_lock():
        counter.value += 1
    with open('files/pongs.txt', 'w') as f:
        print('saving pong...')
        f.write(f'pongs: {counter.value}')
    return f'pong {counter.value}'


if __name__ == '__main__':
    app.run(processes=5)