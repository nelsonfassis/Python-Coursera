grade = raw_input("Please insert your grade: ")
try:
    grade = float(grade)
except:
    print "Invalid input, please enter a number"
    quit()

if grade < 0.0:
    print "Invalid number, your input must be greater or equal to 0.0"
elif grade < 0.6:
    print "F"
elif grade < 0.7:
    print "D"
elif grade < 0.8:
    print "C"
elif grade < 0.9:
    print "B"
elif grade > 1.0:
    print "Invalid number, your input must be less or equal to 1.0"
elif grade >= 0.9:
	print "A"
