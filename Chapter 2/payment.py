#This code means to calculate the gross payment#

name = raw_input("What is your name? ")
worked_hours = raw_input("Enter how many hours were worked: ")
rate = raw_input("Enter what is the payment rate: ")
payment = float(worked_hours) * float(rate)

print "Hi",name + ". Your payment this week is: R$",payment