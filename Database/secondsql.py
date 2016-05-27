import sqlite3

conn = sqlite3.connect('count_org.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#file_name = raw_input('Enter file name: ')
#if ( len(file_name) < 1 ) : file_name = 'mbox-short.txt'
file_name = 'mbox.txt'
file_handler = open(file_name)
for line in file_handler:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    #print pieces
    email = pieces[1].split('@')[1]
    #print email
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( email, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (email, ))
    # This commits outstanding changes to disk.
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()