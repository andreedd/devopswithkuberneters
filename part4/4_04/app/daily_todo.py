from multiprocessing import Value
from unicodedata import name
import os
import psycopg2
import uuid
from flask import Flask
import requests
app = Flask(__name__)

import psycopg2.extras
psycopg2.extras.register_uuid()

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres-svc.todo-app",
        database="postgres",
        user=os.environ['POSTGRES_USERNAME'],
        password=os.environ['POSTGRES_PASSWORD'])
    return conn


def add_todo(url):
    conn = get_db_connection()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    print(f'Adding todo with title: {url} to database')
    cur.execute('INSERT INTO todo_todo (id, title)'
            'VALUES (%s, %s )',
            (uuid.uuid4(), f'Read {url}')
            )

    conn.commit()
    cur.close()
    conn.close()
    return


def main():
    response = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    add_todo(response.url)



if __name__ == '__main__':
    main()