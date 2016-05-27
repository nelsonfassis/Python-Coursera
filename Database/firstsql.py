import sqlite3

conn = sqlite3.connect('count_org.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

#file_name = raw_input('Enter file name: ')
#if ( len(file_name) < 1 ) : file_name = 'mbox-short.txt'
file_name = 'mbox-short.txt'
file_handler = open(file_name)
for line in file_handler:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    #print pieces
    email = pieces[1]
    #print email
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) 
                VALUES ( ?, 1 )''', ( email, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', 
            (email, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()