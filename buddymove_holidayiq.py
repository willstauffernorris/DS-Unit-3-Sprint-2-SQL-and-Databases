import pandas as pd
import sqlite3

df = pd.read_csv('https://raw.githubusercontent.com/willstauffernorris/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')

print(df.head(5))
print(df.shape)


connection = sqlite3.connect('dstwelve2.sqlite3')
#df.to_sql('dstwelve2.sqlite3', connection)

cursor = connection.cursor()

query = "SELECT COUNT(*) FROM 'dstwelve2.sqlite3'"
testing = cursor.execute(query).fetchall()[0]

print(testing)