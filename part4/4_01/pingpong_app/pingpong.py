from multiprocessing import Value
from unicodedata import name
import os
import psycopg2
from flask import Flask
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres-svc.log-app",
        database="postgres",
        user=os.environ['POSTGRES_USERNAME'],
        password=os.environ['POSTGRES_PASSWORD'])
    return conn

conn = get_db_connection()
# Open a cursor to perform database operations
cur = conn.cursor()
#https://github.com/psycopg/psycopg2/issues/1200

cur.execute('DROP TABLE IF EXISTS pingpongs;')
cur.execute('CREATE TABLE pingpongs (id serial PRIMARY KEY,'
                                 'count integer NOT NULL);'
                                 )

cur.execute('INSERT INTO pingpongs (count)'
        'VALUES (%s )',
        ([1])
        )

conn.commit()
cur.close()
conn.close()

counter = Value('i', 0)



@app.route('/')
def home():
    return f'Hello pingpong'


@app.route('/pingpong')
def count():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM pingpongs;')
    pingpongs = cur.fetchone()[0]
    cur.execute(f'UPDATE pingpongs SET count={pingpongs + 1};')
    conn.commit()
    cur.close()
    conn.close()
    return f'pong {pingpongs}'


if __name__ == '__main__':
    app.run(processes=5)