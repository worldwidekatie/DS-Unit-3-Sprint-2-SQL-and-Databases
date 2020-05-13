import psycopg2
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv() #installs stuff from the env enviornment

 # Connect to the PostgresSQL database
DB_NAME=os.getenv('DB_NAME', default='OOPS')
DB_USER=os.getenv('DB_USER', default='OOPS')
DB_PW=os.getenv('DB_PW', default='OOPS')
DB_HOST=os.getenv('DB_HOST', default='OOPS')

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PW, host=DB_HOST)
cur = conn.cursor()

query = "SELECT count(index_label) FROM titanic_table"
cur.execute(query)
result = cur.fetchall()

print("--------------------------")
print("Titanic Report")
print("--------------------------")
print("This database should have 887 rows.")
print("This database has", result[0][0], "rows!")
print("--------------------------")
query = "SELECT AVG(age) FROM titanic_table"
cur.execute(query)
result = cur.fetchall()
print("The average passenger age is ", round(result[0][0]))
print("--------------------------")
query = "SELECT AVG(survived) FROM titanic_table"
cur.execute(query)
result = cur.fetchall()
print(format(result[0][0], ".2%"), "of passengers survived")
print("--------------------------")