fname = raw_input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    
    for obj in line.split():
        if obj not in lst:
            lst.append(obj)
        else: continue
       
lst.sort()
print lst