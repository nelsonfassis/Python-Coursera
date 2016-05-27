#Caculating the payment with ensurance#


try:
    worked_hours = raw_input("Please type the amount of hours worked this week: ")
    float_hours = float(worked_hours)
    rate = raw_input("Please input your payment rate: ")
    float_rate = float(rate)
    if float_hours <= 40:
        payment = float_hours * float_rate
        print "Your weekly payment will be C$:",payment
    else:
        extra_hours = (float_hours - 40)
        extra_payment = extra_hours * (float_rate * 1.5)
        payment = ((float_hours - extra_hours) * float_rate) + extra_payment
        print "Your weekly payment will be C$:",payment
except:
    print "Invalid values!"


