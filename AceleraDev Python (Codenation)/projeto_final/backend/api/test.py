import sqlite3

#dir db
db_path = './db.sqlite3'

#connect with db.sqlite3
sqliteConnection = sqlite3.connect(db_path)
cursor = sqliteConnection.cursor()

#query test
""" query = 'SELECT * FROM api_user;'
cursor.execute(query)
record = cursor.fetchall()
print(record)
cursor.close() """