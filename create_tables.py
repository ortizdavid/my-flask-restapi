import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE  users(id INTEGER primary key, username varchar(50), password varchar(50));"
cursor.execute(create_table)

create_table = "CREATE TABLE  items(name VARCHAR(50), price real);"
cursor.execute(create_table)

connection.commit()
connection.close()