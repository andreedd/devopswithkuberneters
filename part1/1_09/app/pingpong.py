from multiprocessing import Value
from unicodedata import name

counter = Value('i', 0)

from flask import Flask
app = Flask(__name__)

@app.route('/pingpong')
def count():
    with counter.get_lock():
        counter.value += 1
    return f'pong {counter.value}'

if __name__ == '__main__':
    app.run(processes=5)