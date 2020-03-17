import sqlite3


DB_FILEPATH = 'rpg_db.sqlite3'

connection = sqlite3.connect(DB_FILEPATH)
#connection.row_factory = sqlite3.Row
print('CONNECTION', connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = 'SELECT COUNT(*) FROM charactercreator_character'

result = cursor.execute(query).fetchall()
print('How many total Characters are there?', result)


query2 = 'SELECT COUNT(*) FROM charactercreator_cleric'

result2 = cursor.execute(query2).fetchall()
print('How many of each specific subclass?')
print('How many Clerics?', result2)
### Could just repeat this code, but 
###There must be a more elegant way to grab all five subclasses


### How many total Items?
query_items = 'SELECT COUNT(*) FROM armory_item'
result_items = cursor.execute(query_items).fetchall()
print(f'Number of items {result_items}')


#How many of the Items are weapons? How many are not?
query_weapons = '''
SELECT count(*) 
FROM armory_item
JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
'''

result_weapons = cursor.execute(query_weapons).fetchall()
print(f'Number of items that are weapons {result_weapons}')


#How many Items does each character have? (Return first 20 rows)
#How many Weapons does each character have? (Return first 20 rows)
#On average, how many Items does each Character have?
#On average, how many Weapons does each character have?