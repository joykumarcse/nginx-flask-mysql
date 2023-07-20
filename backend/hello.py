import os
from flask import Flask
import pymysql


class DBManager:
    def __init__(self, database='example', host="db", user="root", password=None):
        self.connection = pymysql.connect(
            user=user,
            password=password,
            host=host,
            database=database,
            autocommit=True
        )
        self.cursor = self.connection.cursor()
    
    def populate_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,5)])
        self.connection.commit()
    
    def query_titles(self):
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec


server = Flask(__name__)
conn = None

@server.route('/')
def listBlog():
    global conn
    if not conn:
        password = os.environ.get("MYSQL_ROOT_PASSWORD")
        if not password:
            return "MySQL root password not set in environment variables.", 500

        conn = DBManager(password=password)
        conn.populate_db()
    rec = conn.query_titles()

    response = ''
    for c in rec:
        response = response  + '<div>   Hello  ' + c + '</div>'
    return response


if __name__ == '__main__':
    password = os.environ.get("MYSQL_ROOT_PASSWORD")
    server.run(host='0.0.0.0')
