name = raw_input("Enter file:")
#name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        hour = words[5].split(":")
        count[hour[0]] = count.get(hour[0],0)+1
    else: continue
lst = list()

for key,value in count.items():
    lst.append( (key, value) )
lst.sort()

for key, value in lst:
    print key, value


