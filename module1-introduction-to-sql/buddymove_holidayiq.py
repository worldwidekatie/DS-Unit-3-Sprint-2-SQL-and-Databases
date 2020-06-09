# import sqlite3
# import os
# import pandas as pd

# df = pd.read_csv('buddymove_holidayiq.py')
# print(df.head())


# #DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

# #conn = sqlite3.connect(DATABASE_FILEPATH)

import sqlite3
import os
import pandas as pd

df = pd.read_csv('module1-introduction-to-sql/buddymove_holidayiq.csv')
df.columns = ['user_id', 'sports', 'religious', 'nature', 'theatre', 
'shopping', 'picnic']
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
df.to_sql('df', conn, if_exists='replace', index=False)

# Q1: Count how many rows you have - it should be 249
query = 'SELECT count(user_id) FROM df'
result = curs.execute(query).fetchall()
print("This database should have 249 rows.")
print("This database has", result[0][0], "rows!")

# Q2: How many users who reviewed at least 100 nature in the
# category also reviewed at least 100 in the shopping category?

query = """SELECT count(user_id), nature, shopping FROM df
            Where nature >= 100 AND shopping >=100
            """
result = curs.execute(query).fetchall()
print(result[0][0], "Users reviewed at least 100 in the shopping and nature categories")