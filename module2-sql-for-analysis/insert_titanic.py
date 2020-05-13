"""Then, set up a new table for the Titanic data (titanic.csv) - 
spend some time thinking about the schema to make sure it is 
appropriate for the columns. Enumerated types may be useful. 
Once it is set up, write a insert_titanic.py script that 
uses psycopg2 to connect to and upload the data from the csv, 
and add the file to your repo. 

Then start writing PostgreSQL queries to explore the data!"""
import psycopg2
import os
import json
from dotenv import load_dotenv
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

load_dotenv()

 # Connect to the PostgresSQL database
DB_NAME=os.getenv('DB_NAME', default='OOPS')
DB_USER=os.getenv('DB_USER', default='OOPS')
DB_PW=os.getenv('DB_PW', default='OOPS')
DB_HOST=os.getenv('DB_HOST', default='OOPS')

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PW, host=DB_HOST)
cur = conn.cursor()


# Create a new PostgresSQL table
create_titanic_table = """
CREATE TABLE IF NOT EXISTS titanic_table(
    index_label SERIAL PRIMARY KEY,
    survived INT,
    class INT,
    name VARCHAR(200),
    sex VARCHAR(30),
    age FLOAT,
    sib_spouses INT,
    parent_children INT,
    fare FLOAT
);
"""
cur.execute(create_titanic_table)
conn.commit()

# Turn CSV into pandas dataframe then PostgresSQL
df = pd.read_csv('titanic.csv')
df.columns = ['survived', 'class', 'name', 'sex', 
'age', 'sib_spouses', 'parent_children', 'fare']
df['name'] = df['name'].str.replace("'", " ")
print(df.head())

engine = create_engine('sqlite://', echo=False)
df.to_sql('titanic_df', engine, if_exists='replace', 
index=True)
titanic_df = engine.execute("SELECT * FROM titanic_df")
print(type(titanic_df))

# Insert passenger into the new table.
for passenger in titanic_df:
    insert_passenger = f"""
    INSERT INTO titanic_table
    (index_label,
    survived,
    class,
    name,
    sex,
    age,
    sib_spouses,
    parent_children,
    fare)
    VALUES{passenger}; """
    cur.execute(insert_passenger)
conn.commit()

#This is not working. It works in TablePlus but not here
query = "SELECT count(index_label) FROM titanic_table"
result = cur.execute(query).fetchall()
print("This database should have 887 rows.")
print("This database has", result[0][0], "rows!")