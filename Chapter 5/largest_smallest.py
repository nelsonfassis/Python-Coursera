largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
        if largest == None:
            largest = num
        if smallest == None:
            smallest = num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    except:
        print "Invalid input"
        continue
print "Maximum is",largest
print "Minimum is",smallest