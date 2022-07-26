#!/usr/bin/env python3

import requests
import os

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():    
    return render_template('index.html')


@app.route("/todos", methods = ['POST', 'GET'])
def todos():
    todos = {}
    backend_url = os.environ.get('BACKEND_URL', 'http://localhost:8005')
    if request.method == 'POST':
      post_data = {'todo': request.form['todo']}
      print(post_data)
      response = requests.post(f'{backend_url}/todo/todos/', json=post_data)
    else:
      response = requests.get(f'{backend_url}/todo/todos/')
    
    todos = response.json()
    print(f'response content: {todos}')
    return render_template('todos.html', todos=todos['data'])



if __name__ == "__main__":
    pass