##stuff = dict()
##print stuff.get('candy',-1) -1

#name = raw_input("Enter file:")
name = "mbox-short.txt"
#if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender = dict()
for line in handle:
    if line.startswith("From "):
        mails = line.split()
        mail = mails[1]
        sender[mail] = sender.get(mail,0)+1
    else: continue

who = 0
amount = 0
for key in sender:
    if sender[key] > amount:
        amount = sender[key]
        who = key
    else: continue

print who,amount