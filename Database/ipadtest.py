import sqlite3
import json

cli_name = raw_input("Insert client name :")
cli_birthday= raw_input(" Insert birthday (DD/MM/YY) :")

conn = sqlite3.connect("clientdb.sqlite")
cur = conn.cursor()

print (cli_name,cli_birthday)

cur.execute('''CREATE TABLE IF NOT EXISTS Clients (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
birthday TEXT)''')

cur.execute('''INSERT OR REPLACE INTO Clients (name, birthday) VALUES ( ?, ? )''',(cli_name, cli_birthday))

print (cur.execute('''SELECT Clients.name FROM Clients'''))
