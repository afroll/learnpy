import sqlite3
conn = sqlite3.connect('data.db')
cur = conn.cursor()
query = "CREATE TABLE IF NOT EXISTS films (id INT, title TEXT, duration INT)"
cur.execute(query)

insert_query = "INSERT INTO films VALUES(1, 'LOTR', 220)"
cur.execute(insert_query)
conn.commit()

select_query = "SELECT * FROM films"
for row in  cur.execute(select_query):
    print(row)