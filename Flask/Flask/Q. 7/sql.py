import sqlite3

conn = sqlite3.connect('c:/Users/RS/OneDrive/Documents/DS/Ineuron Assignment/Flask/Q. 7/school.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, addr TEXT, city TEXT, pin INTEGER, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)')
print("Table created successfully")
conn.close()

