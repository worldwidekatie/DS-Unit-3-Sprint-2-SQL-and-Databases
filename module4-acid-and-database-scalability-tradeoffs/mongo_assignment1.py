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
titanic_table = client.titanic_table

 # Connect to the PostgresSQL database
DB_NAME=os.getenv('DB_NAME', default='OOPS')
DB_USER=os.getenv('DB_USER', default='OOPS')
DB_PW=os.getenv('DB_PW', default='OOPS')
DB_HOST=os.getenv('DB_HOST', default='OOPS')

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PW, host=DB_HOST)
cur = conn.cursor()
get_passengers = "SELECT * FROM titanic_table"
cur.execute(get_passengers)
passengers = cur.fetchall()

# Putting all that into Mongo
for passenger in passengers:
    passenger_ = {
    'index_label': passenger[0],
    'survived': passenger[1],
    'class': passenger[2],
    'name': passenger[3],
    'sex': passenger[4],
    'age': passenger[5],
    'sib_spouses': passenger[6],
    'parent_children': passenger[7],
    'fare': passenger[8]}
    titanic_table.test.insert_one(passenger_)

# Testing
print(titanic_table.test.count_documents({'index_label': 886, 'survived': 0, 'class': 3, 'name': 'Mr. Patrick Dooley', 'sex': 'male', 'age': 32.0, 'sib_spouses': 0, 'parent_children': 0}))
print(titanic_table.test.count_documents({'index_label': 880, 'survived': 0, 'class': 3, 'name': 'Mr. Henry Jr Sutehall', 'sex': 'male', 'age': 25.0, 'sib_spouses': 0, 'parent_children': 0}))
print(titanic_table.test.count_documents({'index_label': 859, 'survived': 0, 'class': 3, 'name': 'Miss. Dorothy Edith Sage', 'sex': 'female', 'age': 14.0, 'sib_spouses': 8, 'parent_children': 2}))
print(titanic_table.test.count_documents({'index_label': 787, 'survived': 0, 'class': 2, 'name': 'Mr. Alfred Gaskell', 'sex': 'male', 'age': 16.0, 'sib_spouses': 0, 'parent_children': 0}))
print(titanic_table.test.count_documents({'index_label': 138, 'survived': 0, 'class': 1, 'name': 'Mr. Victor Giglio', 'sex': 'male', 'age': 24.0, 'sib_spouses': 0, 'parent_children': 0}))

