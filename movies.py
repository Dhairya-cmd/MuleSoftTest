import sqlite3

												#connection
cnt = sqlite3.connect("bollywood.db")
print('Connection established Successfully')

												#create table
cnt.execute('''CREATE TABLE movies(
name TEXT,
actor TEXT,
actress TEXT,
yearOfRelease INTEGER)''')
print("Table Created Successfully")


												#insert record
cnt.execute('''INSERT INTO movies VALUES(
'RRR', 'Ramcharan', 'Alia Bhatt', 2022);''')
cnt.commit()
print("Record Insert Successfully")

												#fetch record
cursor=cnt.execute("SELECT * FROM movies WHERE actor = 'Allu Arjun'")
print(cursor.fetchall())

												#fetch record with filter
cursor=cnt.execute("SELECT * FROM movies WHERE actor = 'Allu Arjun'")
print(cursor.fetchall())
