import psycopg2

DATABASE_HOST='db'
DATABASE_USER='postgres'
DATABASE_PASSWORD='mysecretpassword'
DATABASE_NAME='postgres'

conn = psycopg2.connect(
    dbname=DATABASE_NAME,
    user=DATABASE_USER,
    host=DATABASE_HOST,
    password=DATABASE_PASSWORD
)

cur = conn.cursor()
cur.execute("""CREATE TABLE author (
    author_id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR
);""")
# cur.execute("""CREATE TABLE users (
#     author_id INTEGER NOT NULL PRIMARY KEY,
#     first_name VARCHAR,
#     last_name VARCHAR
# );""")
conn.commit()
cur.close()
conn.close()