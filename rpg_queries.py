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

## Another way to select how many items are weapons
query_weapons2 = '''
SELECT
sum(w.item_ptr_id is null) as non_weapon
,sum(w.item_ptr_id is not null) as weapon

FROM armory_item i
LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id
''' 
result_weapons2 = cursor.execute(query_weapons2).fetchall()
print(f'Number of items that are not weapons, number that are weapons: {result_weapons2}')
#print(f'Number of items that are not weapons {result_weapons2[0]}')
#There must be a better way to do this syntax: how can I access the first index of my 'result_weapons2'?



#How many Items does each character have? (Return first 20 rows)
query_num_items = '''
SELECT
c.character_id,
c.name as char_name,
count(inv.item_id) as item_count,
count(w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id

GROUP BY c.character_id
ORDER BY item_count DESC
LIMIT 20
'''

result_num_items = cursor.execute(query_num_items).fetchall()
print(f'how many weapons does each character have?: {result_num_items}')

print('-------------------')

#How many Weapons does each character have? (Return first 20 rows)
query_num_weapons = '''
SELECT
c.character_id,
c.name as char_name,
count(inv.item_id) as item_count,
count(w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id

GROUP BY c.character_id
ORDER BY weapon_count DESC
LIMIT 20
'''

result_num_weapons = cursor.execute(query_num_weapons).fetchall()
print(f'how many weapons does each character have?: {result_num_weapons}')
print('----------------')


#On average, how many Items does each Character have?

query_avg_items = '''

SELECT
	AVG(item_count)
FROM
	(
	SELECT
		c.character_id,
		c.name as char_name,
		count(inv.item_id) as item_count,
		count(w.item_ptr_id) as weapon_count
		
	
	FROM charactercreator_character c
	LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
	LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
	
	GROUP BY c.character_id
	
	)
'''


result_avg_items = cursor.execute(query_avg_items).fetchall()
print(f'On average, how many Items does each Character have?: {result_avg_items}')

#On average, how many Weapons does each character have?
query_avg_weapons = '''

SELECT
	AVG(weapon_count)
FROM
	(
	SELECT
		c.character_id,
		c.name as char_name,
		count(inv.item_id) as item_count,
		count(w.item_ptr_id) as weapon_count
		
	
	FROM charactercreator_character c
	LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
	LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
	
	GROUP BY c.character_id
	
	)
'''


result_avg_weapons = cursor.execute(query_avg_weapons).fetchall()
print(f'On average, how many Weapons does each character have?: {result_avg_weapons}')