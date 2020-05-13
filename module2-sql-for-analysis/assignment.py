"""Reproduce (debugging as needed) the live lecture task of 
setting up and inserting the RPG data into a PostgreSQL database, 
and add the code you write to do so.
"""
import psycopg2
import os
import json
from dotenv import load_dotenv
import pandas as pd
import sqlite3

load_dotenv()

 # Connect to the PostgresSQL database
DB_NAME=os.getenv('DB_NAME', default='OOPS')
DB_USER=os.getenv('DB_USER', default='OOPS')
DB_PW=os.getenv('DB_PW', default='OOPS')
DB_HOST=os.getenv('DB_HOST', default='OOPS')

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PW, host=DB_HOST)

cur = conn.cursor()

create_table_statement = """
CREATE TABLE IF NOT EXISTS test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""

insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'Another row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""

cur.execute(create_table_statement)
cur.execute(insert_statement)
conn.commit()

# Connect to my sqlite3 database
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

#Checking if my row count is correct (302)
row_count = 'SELECT COUNT(*) FROM charactercreator_character'
print(sl_curs.execute(row_count).fetchall())

# GOAL: copy the characters table from SQLite to PostgreSQL using python
# STEP 1 - E=Extract: Get the Characters
get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()
print(characters[:5])
print(len(characters))

# STEP 2 - Transform
# In this case, we don't actually want/need to change much
# Because we want to keep all the data
# And we're going from SQL to SQL
# First we need a new table with the appropriate schema
# The code below finds that.
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

# Make a new table in my PostgresSQL database
create_character_table = """
CREATE TABLE IF NOT EXISTS characters(
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
"""
cur.execute(create_character_table)
conn.commit()

#Insert characters into that new table.
for character in characters:
    insert_character = """
    INSERT INTO characters
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    cur.execute(insert_character)
conn.commit()