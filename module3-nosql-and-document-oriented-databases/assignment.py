"""
"How was working with MongoDB different from working 
with PostgreSQL? What was easier, and what was harder?"

MongoDB needs everything in key value pairs which is odd.
I think I like PostgreSQL better. MongoDB is actually maybe
easier for getting stuff in but it seems harder to work with
and I don't like that it's not picky about duplicate values
or what the keys are in those pairs like if they correspond
to an actual column heading or not. 

It seems like headaches all around later on. I don't trust it.
"""

import pymongo
from dotenv import load_dotenv
import psycopg2
import os
import sqlite3
load_dotenv() #installs stuff from the env enviornment

# Connecting to Mongo
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_uri)
rpg = client.rpg_database

# Connecting to sqlight3 data
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
get_characters = 'SELECT * FROM charactercreator_character'
characters = curs.execute(get_characters).fetchall()

# Putting all that into Mongo
for character in characters:
    character_ = {
    'character_id': character[0],
    'name': character[1],
    'level': character[2],
    'exp': character[3],
    'hp': character[4],
    'strength': character[5],
    'intelligence': character[6],
    'dexterity': character[7],
    'wisdom': character[8]}
    rpg.test.insert_one(character_)

# Checking to see if the first two went in properly
print(rpg.test.count_documents({'character_id': 1, 'name': 'Aliquid iste optio reiciendi', 'level': 0, 'exp': 0, 'hp': 10, 'strength': 1, 'intelligence': 1, 'dexterity': 1, 'wisdom': 1}))
print(rpg.test.count_documents({'character_id': 2, 'name': 'Optio dolorem ex a', 'level': 0, 'exp': 0, 'hp': 10, 'strength': 1, 'intelligence': 1, 'dexterity': 1, 'wisdom': 1}))

