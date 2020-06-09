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

print(" ")
print("--------------------------")
print("Titanic Report Assignment")
print("--------------------------")
print(" ")

print("--------------------------")
print("Q1: How many passengers survived, and how many died?")
query = "SELECT count(survived), survived FROM titanic_table GROUP BY survived"
cur.execute(query)
result = cur.fetchall()
print(result[1][0], "passengers survived.")
print(result[0][0], "passengers perished.")
print("--------------------------")

print(" ")
print("--------------------------")
print("Q2: How many passengers were in each class?")
query = "SELECT count(class), class FROM titanic_table GROUP BY class"
cur.execute(query)
result = cur.fetchall()
print("First class had", result[0][0], "passengers.")
print("Second class had", result[2][0], "passengers.")
print("Third class had", result[1][0], "passengers.")
print("--------------------------")

print(" ")
print("--------------------------")
print("Q3: How many passengers survived/died within each class?")
query = "SELECT count(survived), class FROM titanic_table WHERE survived=1 GROUP BY class"
cur.execute(query)
result = cur.fetchall()

query1 = "SELECT count(survived), class FROM titanic_table WHERE survived=0 GROUP BY class"
cur.execute(query1)
result1 = cur.fetchall()

print(result[0][0], "first-class passengers survived.")
print(result1[0][0], "first-class passengers perished.")
print("--------------------------")
print(result[2][0], "second-class passengers survived.")
print(result1[2][0], "second-class passengers perished.")
print("--------------------------")
print(result[1][0], "third-class passengers survived.")
print(result1[1][0], "third-class passengers perished.")
print("--------------------------")

print(" ")
print("--------------------------")
print("Q4: What was the average age of survivors vs nonsurvivors?")
query = "SELECT AVG(age) FROM titanic_table WHERE survived=1"
cur.execute(query)
result = cur.fetchall()

query1 = "SELECT AVG(age) FROM titanic_table WHERE survived=0"
cur.execute(query1)
result1 = cur.fetchall()

print("The average survivor age was", round(result[0][0]))
print("The average non-survivor age was", round(result1[0][0]))
print("--------------------------")

print(" ")
print("--------------------------")
print("Q5: What was the average age of each passenger class?")
query = "SELECT AVG(age), class FROM titanic_table GROUP BY class"
cur.execute(query)
result = cur.fetchall()

print("The average age for first-class was", round(result[0][0]))
print("The average age for second-class was", round(result[2][0]))
print("The average age for third-class was", round(result[1][0]))
print("--------------------------")


print(" ")
print("--------------------------")
print("Q6: What was the average fare by passenger class? By survival?")
query = "SELECT AVG(fare), class FROM titanic_table GROUP BY class"
cur.execute(query)
result = cur.fetchall()

query1 = "SELECT AVG(fare), survived FROM titanic_table GROUP BY survived"
cur.execute(query1)
result1 = cur.fetchall()

print("The average fare for first-class was $", round(result[0][0], 2))
print("The average fare for second-class was $", round(result[2][0], 2))
print("The average fare for third-class was $", round(result[1][0], 2))
print("--------------------------")
print("The average fare for survivors was $", round(result1[1][0], 2))
print("The average fare for non-survivors was $", round(result1[0][0], 2))
print("--------------------------")


print(" ")
print("--------------------------")
print("Q7: How many siblings/spouses aboard on average, by passenger class? By survival?")
query = "SELECT AVG(sib_spouses), class FROM titanic_table GROUP BY class"
cur.execute(query)
result = cur.fetchall()

query1 = "SELECT AVG(sib_spouses), survived FROM titanic_table GROUP BY survived"
cur.execute(query1)
result1 = cur.fetchall()

print("The average # of siblings/spouses for first-class was", round(result[0][0], 2))
print("The average # of siblings/spouses for second-class was", round(result[2][0], 2))
print("The average # of siblings/spouses for third-class was", round(result[1][0], 2))
print("--------------------------")
print("The average # of siblings/spouses for survivors was", round(result1[1][0], 2))
print("The average # of siblings/spouses for non-survivors was", round(result1[0][0], 2))
print("--------------------------")

print(" ")
print("--------------------------")
print("Q8: How many parents/children aboard on average, by passenger class? By survival?")
query = "SELECT AVG(parent_children), class FROM titanic_table GROUP BY class"
cur.execute(query)
result = cur.fetchall()

query1 = "SELECT AVG(parent_children), survived FROM titanic_table GROUP BY survived"
cur.execute(query1)
result1 = cur.fetchall()

print("The average # of parents/children for first-class was", round(result[0][0], 2))
print("The average # of parents/children for second-class was", round(result[2][0], 2))
print("The average # of parents/children for third-class was", round(result[1][0], 2))
print("--------------------------")
print("The average # of parents/children for survivors was", round(result1[1][0], 2))
print("The average # of parents/children for non-survivors was", round(result1[0][0], 2))
print("--------------------------")

# print(" ")
# print("--------------------------")
# print("Q9: Do any passengers have the same name?")
# query = "SELECT AVG(survived) FROM titanic_table"
# cur.execute(query)
# result = cur.fetchall()
# print(format(result[0][0], ".2%"), "of passengers survived")
# print("--------------------------")

# print(" ")
# print("--------------------------")
# print("STRETCH: How many married couples were aboard the Titanic?")
# # (Bonus! Hard, may require pulling and processing with Python) 
# # Assume that two people (one Mr. and one Mrs.) with the same last name and 
# # with at least 1 sibling/spouse aboard are a married couple.
# query = "SELECT AVG(survived) FROM titanic_table"
# cur.execute(query)
# result = cur.fetchall()
# print(format(result[0][0], ".2%"), "of passengers survived")
# print("--------------------------")

print(" ")
print("--------------------------")
print("End of Assignment")
print("--------------------------")