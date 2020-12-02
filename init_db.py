import sqlite3

connection=sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur=connection.cursor()
cur.execute("INSERT INTO posts(title,content) VALUES(?,?)",
            ('First Baby Step','Every step counts')
            )
cur.execute("INSERT INTO posts(title,content) VALUES(?,?)",
            ('Second Baby Step','Every failure counts')
            )
connection.commit()
connection.close()
