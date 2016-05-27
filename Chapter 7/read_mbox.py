#Assignement 7.2
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
line_count = 0
number_sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line_count = line_count + 1
    number_start = line.find(":")
    number = float(line[(number_start + 1):].strip())
    number_sum = (number_sum + number)
print "Average spam confidence:",  (number_sum / line_count )
#print "Done"