
import requests
import os

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def main():
    url = os.getenv('URL', 'https://example.com')
    #url = request.args.get('url', 'https://example.com')
    data = requests.get(url)
    return data.content

if __name__ == '__main__':
    app.run()