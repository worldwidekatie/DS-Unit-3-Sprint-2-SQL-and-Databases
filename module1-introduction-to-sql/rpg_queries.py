import sqlite3
import os

DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

conn = sqlite3.connect(DATABASE_FILEPATH)
#conn.row_factory = sqlite3.Row
print(type(conn))

curs = conn.cursor()
print(type(curs))

# Q1: How many total Characters are there?
query = 'SELECT COUNT(character_id) FROM charactercreator_character;'
result = curs.execute(query).fetchall()
print('---------------')
print("RPG Report")
print('---------------')
print( " ")
print('---------------')
print("Character Summary")
print('---------------')
print("There are ", result[0][0], "Total Characters Including:")

# Q2: How many of each specific subclass?
query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'
result = curs.execute(query).fetchall()
print(result[0][0], "Clerics")

query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'
result = curs.execute(query).fetchall()
print(result[0][0], "Fighters")

query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'
result = curs.execute(query).fetchall()
print(result[0][0], "Thieves")

query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage;'
result = curs.execute(query).fetchall()
print(result[0][0], "Mages")

query = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;'
result = curs.execute(query).fetchall()
print("and", result[0][0], "Mages are Necromancers")


# Q3: How many total items?
query6 = 'SELECT COUNT(item_id) FROM armory_item;'
result = curs.execute(query6).fetchall()
print( " ")
print('---------------')
print("Items Summary")
print('---------------')
print("There are", result[0][0], "Total Items")


# Q4: How many of the items are weapons? How many are not?
query = 'SELECT COUNT(item_ptr_id) FROM armory_weapon;'
result1 = curs.execute(query).fetchall()
print(result1[0][0], "Items are Weapons")
print(result[0][0] - result1[0][0], "Items are not Weapons")

# Q5: How many Items does each character have? (Return first 20 rows)
query = """SELECT 
  charactercreator_character.character_id
  ,charactercreator_character.name
  ,charactercreator_character_inventory.character_id
  ,count(distinct charactercreator_character_inventory.item_id) as number_of_items
FROM charactercreator_character_inventory
JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id
GROUP BY charactercreator_character.name
LIMIT 20;"""
print( " ")
print('---------------')
print("Character Item Counts, First 20")
print('---------------')
result = curs.execute(query).fetchall()
print("Item Counts")
for row in result:
    print(row[1],"has", row[3], "item(s)")

# Q6: How many Weapons does each character have? (Return first 20 rows)
query = """SELECT 
  charactercreator_character.character_id
  ,charactercreator_character.name
  ,charactercreator_character_inventory.character_id
  ,charactercreator_character_inventory.item_id
  ,armory_weapon.item_ptr_id
  ,count(armory_weapon.item_ptr_id) as number_of_weapons
FROM charactercreator_character_inventory
JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character.name
LIMIT 20;"""
print( " ")
print('---------------')
print("Character Weapon Counts, First 20")
print('---------------')
result = curs.execute(query).fetchall()
for row in result:
    print(row[1],"has", row[5], "weapon(s)")

# Q7: On average, how many Items does each character have?
query = """SELECT
	AVG(number_of_items)
FROM(
SELECT 
  charactercreator_character.character_id
  ,charactercreator_character.name
  ,charactercreator_character_inventory.character_id
  ,count(distinct charactercreator_character_inventory.item_id) as number_of_items
FROM charactercreator_character_inventory
JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id
GROUP BY charactercreator_character.name
LIMIT 20) subq;"""

print( " ")
print('---------------')
print("Item Averages")
print('---------------')
result = curs.execute(query).fetchall()
print("Characters have", result[0][0], "Items on average")

# Q8: On average, how many Weapons does each character have?
query = """SELECT
	AVG(number_of_weapons)
FROM(
SELECT 
  charactercreator_character.character_id
  ,charactercreator_character.name
  ,charactercreator_character_inventory.character_id
  ,charactercreator_character_inventory.item_id
  ,armory_weapon.item_ptr_id
  ,count(armory_weapon.item_ptr_id) as number_of_weapons
FROM charactercreator_character_inventory
JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character.name
LIMIT 20) subq;"""

result = curs.execute(query).fetchall()
print("Characters have", result[0][0], "Weapons on average")

print( " ")
print('---------------')
print("End of Report")
print('---------------')
