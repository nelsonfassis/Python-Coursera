import sqlite3

conn = sqlite3.connect("einloge.sqlite")
cur = conn.cursor()

def add_client():
	print "To break the loop, do not insert any value into the Client name"
	while True:
		client_name = raw_input("Insert client name: ")
		if len(client_name) <= 1 : whatodo()
		client_cpf = input("Inser client CPF: ")
		client_company = raw_input("Insert client's company name: ").lower()
		print client_company
		cur.execute('''INSERT OR IGNORE INTO Clients (name, cpf, company_id) VALUES (?,?,?)''', (client_name,client_cpf,client_company) )		
		conn.commit()
		
def add_company():
	print "To break the loop, do not insert any value into the Company name"
	while True:
		company_name = raw_input("Insert company name: ")
		if len(company_name) <= 1 : whatodo()
		company_cnpj = input("Inser CNPJ: ")
		print company_name, company_cnpj
		cur.execute('''INSERT OR IGNORE INTO Company(name, cnpj) values (?,?)''',(company_name,company_cnpj))
		conn.commit()

def show_users():
	for row in cur.execute('''
	SELECT Clients.name, Company.name FROM Clients JOIN Company ON Clients.company_id = Company.id
	'''):
		print row
		
def whatodo():
	print ("What would you like to do?")
	print ("1 - Register a company \n2 - Register a user\n3 - Show users\n4 - Exit")
	try : decision = int(raw_input("I would like to: "))
	except: print ("Insert a numeric value")
	if decision == 1:
		add_company()
		
	if decision == 2:
		add_client()
	if decision == 3:
		show_users()
		whatodo()
	if decision == 4: quit()
	else: print("Invalid input")
			

cur.executescript('''
CREATE TABLE IF NOT EXISTS Clients
(
id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name	TEXT, 
cpf	INTEGER,
company_id INTEGER
);

CREATE TABLE IF NOT EXISTS Company
(
id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT, 
cnpj INTEGER)
''')

whatodo()
