import sqlite3

conn = sqlite3.connect('testequiz.sqlite')
cur = conn.cursor()

org = "Testemd"
cur.executescript =('''CREATE TABLE Counts (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    org    TEXT UNIQUE
    );

	INSERT into Counts (org)
	VALUES( ?, )''', (org, ) )

cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
row = cur.fetchone()