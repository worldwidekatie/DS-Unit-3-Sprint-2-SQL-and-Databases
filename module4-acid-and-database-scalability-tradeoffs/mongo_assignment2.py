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

# Functions
def average(list1, avg_var):
    num = 0
    den = 0
    for i in list1:
        num += i[avg_var]
        den += 1
    result = num/den
    return result

# Begin the Report
print(" ")
print("--------------------------")
print("Titanic MongoDB Report Assignment")
print("--------------------------")
print(" ")

print("--------------------------")
print("Q1: How many passengers survived, and how many died?")
survived = titanic_table.test.count_documents({'survived': 1})
perished = titanic_table.test.count_documents({'survived': 0})
print(survived, "passengers survived.")
print(perished, "passengers perished.")
print("--------------------------")

print(" ")
print("--------------------------")
print("Q2: How many passengers were in each class?")
first = titanic_table.test.count_documents({'class': 1})
second = titanic_table.test.count_documents({'class': 2})
third = titanic_table.test.count_documents({'class': 3})
print("First class had", first, "passengers.")
print("Second class had", second, "passengers.")
print("Third class had", third, "passengers.")
print("--------------------------")

print(" ")
print("--------------------------")
print("Q3: How many passengers survived/died within each class?")
query = "SELECT count(survived), class FROM titanic_table WHERE survived=1 GROUP BY class"
first_s = titanic_table.test.count_documents({'class': 1, 'survived': 1})
second_s = titanic_table.test.count_documents({'class': 2, 'survived': 1})
third_s = titanic_table.test.count_documents({'class': 3, 'survived': 1})

first_p = titanic_table.test.count_documents({'class': 1, 'survived': 0})
second_p = titanic_table.test.count_documents({'class': 2, 'survived': 0})
third_p = titanic_table.test.count_documents({'class': 3, 'survived': 0})

print(first_s, "first-class passengers survived.")
print(first_p, "first-class passengers perished.")
print("--------------------------")
print(second_s, "second-class passengers survived.")
print(second_p, "second-class passengers perished.")
print("--------------------------")
print(third_s, "third-class passengers survived.")
print(third_p, "third-class passengers perished.")
print("--------------------------")

print(" ")
print("--------------------------")
print("Q4: What was the average age of survivors vs nonsurvivors?")
survived = list(titanic_table.test.find({'survived': 1}))
perished = list(titanic_table.test.find({'survived': 0}))

print("The average age of survivors was", round(average(survived, 'age')))
print("The average age of nonsurvivors was", round(average(perished, 'age')))
print("--------------------------")

print(" ")
print("--------------------------")
print("Q5: What was the average age of each passenger class?")
first = list(titanic_table.test.find({'class': 1}))
second = list(titanic_table.test.find({'class': 2}))
third = list(titanic_table.test.find({'class': 3}))

print("The average age for first-class was", round(average(first, 'age')))
print("The average age for second-class was", round(average(second, 'age')))
print("The average age for third-class was", round(average(third, 'age')))
print("--------------------------")


print(" ")
print("--------------------------")
print("Q6: What was the average fare by passenger class? By survival?")

print("The average fare for first-class was $", round(average(first, 'fare'), 2))
print("The average fare for second-class was $", round(average(second, 'fare'), 2))
print("The average fare for third-class was $", round(average(third, 'fare'), 2))
print("--------------------------")
print("The average fare for survivors was $", round(average(survived, 'fare'), 2))
print("The average fare for non-survivors was $", round(average(perished, 'fare'), 2))
print("--------------------------")


print(" ")
print("--------------------------")
print("Q7: How many siblings/spouses aboard on average, by passenger class? By survival?")

print("The average # of siblings/spouses for first-class was", round(average(first, 'sib_spouses'), 2))
print("The average # of siblings/spouses for second-class was", round(average(second, 'sib_spouses'), 2))
print("The average # of siblings/spouses for third-class was", round(average(third, 'sib_spouses'), 2))
print("--------------------------")
print("The average # of siblings/spouses for survivors was", round(average(survived, 'sib_spouses'), 2))
print("The average # of siblings/spouses for non-survivors was", round(average(perished, 'sib_spouses'), 2))
print("--------------------------")

print(" ")
print("--------------------------")
print("Q8: How many parents/children aboard on average, by passenger class? By survival?")

print("The average # of parents/children for first-class was", round(average(first, 'parent_children'), 2))
print("The average # of parents/children for second-class was", round(average(second, 'parent_children'), 2))
print("The average # of parents/children for third-class was", round(average(third, 'parent_children'), 2))
print("--------------------------")
print("The average # of parents/children for survivors was", round(average(survived, 'parent_children'), 2))
print("The average # of parents/children for non-survivors was", round(average(perished, 'parent_children'), 2))


print(" ")
print("--------------------------")
print("Q9: Do any passengers have the same name?")
everyone = list(titanic_table.test.find({'survived': 1, 'survived': 0}))
everyone10 = everyone[:10]

def name_match(list2):
    names1 = []
    names = []
    non_unique = []
    all_names = []
    very_non_unique =[]

    # Start by making a cleaned up nested list of all names
    for i in list2:
        name = i['name']
        name = name.lower()
        name = name.replace('(','').replace(')','').replace('.','')
        name = str.split(name)
        names.append(name)

    # Then make a non-nested list taking out mr mrs etc
    for n in names:
        for i in n:
            if i not in ['mrs', 'mr','miss', 'master', 'j', 'a', 'rev', 'van', 'h', 'jr', 'dr', 'o', 'de', 'd']:
                names1.append(i)

    # Then find the unique ones
    for n in names1:
        if n not in all_names:
            all_names.append(n)
        elif n not in non_unique:
            non_unique.append(n)
        else:
            very_non_unique.append(n)

    
    print(len(non_unique), "names appear at least twice, including:")
    print(non_unique)

print(name_match(everyone))
print("--------------------------")

# print(" ")
# print("--------------------------")
# print("STRETCH: How many married couples were aboard the Titanic?")
# # (Bonus! Hard, may require pulling and processing with Python) 
# # Assume that two people (one Mr. and one Mrs.) with the same last name and 
# # with at least 1 sibling/spouse aboard are a married couple.
# print("--------------------------")

print(" ")
print("--------------------------")
print("End of Assignment")
print("--------------------------")