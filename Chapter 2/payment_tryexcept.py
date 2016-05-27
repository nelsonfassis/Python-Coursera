#Caculating the payment with ensurance#

worked_hours = raw_input("Please type the amount of hours worked this week: ")
try:
    float_hours = float(worked_hours)
except:
    print "You entered an invalid value!"
    float_hours = "invalid"
rate = raw_input("Please input your payment rate: ")
try:
    float_rate = float(rate)
except:
    print "You entered an invalid value!"
    float_rate = "invalid"
    
if type(float_hours) == str:
    print "Invalid values entered! Aborting operation."
elif type(float_rate) == str:
    print "Invalid values entered! Aborting operation."
else:
    if float_hours <= 40:
        payment = float_hours * float_rate
        print "Your weekly payment will be C$:",payment
    else:
        extra_hours = (float_hours - 40)
        extra_payment = extra_hours * (float_rate * 1.5)
        payment = ((float_hours - extra_hours) * float_rate) + extra
        print "Your weekly payment will be C$:",payment
    
