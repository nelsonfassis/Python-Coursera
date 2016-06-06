import sqlite3

conn = sqlite3.connect("einloge.sqlite")
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Clients''')

cur.execute('''
CREATE TABLE Clients
(id INTENGER PRIMARY KEY NOT NULL,
name TEXT, 
cpf INTEGER,
company_id
)''')

print "To break the loop, do not insert any value into the Client name"
while True:
	client_name = raw_input("Insert client name: ")
	if client_name <= 1: break
	client_cpf = input("Inser client CPF: ")
	client_company = raw_input("Insert client's company name: ").lower()
	print client_company

cur.commit()
