import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id int, username text, password text)"
cursor.execute(create_table)

# add a user
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# add multiple users
users = [
    (2, 'rolf', 'asdf'),
    (3, 'james', 'xyz')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()