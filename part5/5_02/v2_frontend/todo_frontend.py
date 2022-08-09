#!/usr/bin/env python3

import requests
import os

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():    
    return render_template('index.html')


@app.route("/todos", methods = ['POST', 'GET'])
@app.route("/todos/<id>", methods = ['GET'])
def todos(id=None):
    todos = {}
    backend_url = os.environ.get('BACKEND_URL', 'http://localhost:8005')
    if id: # PUT
      put_data = {'todo_id': id}
      print(put_data)
      response = requests.put(f'{backend_url}/todo/todos/', json=put_data)
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