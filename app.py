import psycopg2
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World from Linda in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lmaccagnan_lab10_user:JjDu8GuXYBAwv40n5iKYfQLpnBp5PRVl@dpg-d75al3f5r7bs73b1okd0-a/lmaccagnan_lab10")
    conn.close()
    return 'Database connection successful!'

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://lmaccagnan_lab10_user:JjDu8GuXYBAwv40n5iKYfQLpnBp5PRVl@dpg-d75al3f5r7bs73b1okd0-a/lmaccagnan_lab10")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Created!'
    

