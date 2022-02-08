
import sqlite3


cnt = sqlite3.connect("bollywood")


cnt.execute('''CREATE TABLE movies(
name TEXT,
actor TEXT,
actress TEXT,
yearOfRelease INTEGER,);''')

cnt.execute('''INSERT INTO movies VALUES(
'Pushpa', 'Allu Arjun', 'Rashmika Mandana', 2021);''')

cnt.commit()


cnt.execute('SELECT * FROM movies')

cnt.execute('SELECT * FROM movies WHERE actor = 'Allu Arjun'')
