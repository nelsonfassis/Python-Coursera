fname = raw_input("Enter file name: ")
#fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        
        print line.split()[1]
        count += 1
    else: continue
print "There were", count, "lines in the file with From as the first word"
