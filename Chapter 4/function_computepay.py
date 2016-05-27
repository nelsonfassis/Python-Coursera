#Caculating the payment with ensurance#
def wrg_inp():
        print "You entered an invalid value!"
        quit()
def computepay(hours,rate):   
    if hours <= 40:
        payment = hours * rate
        return payment
    else:
        extra_hours = (hours - 40)
        extra_payment = extra_hours * (rate * 1.5)
        payment = ((hours - extra_hours) * rate) + extra_payment
        return payment       
        
worked_hours = raw_input("Please type the amount of hours worked this week: ")
try:
    hours = float(worked_hours)
except:
    wrg_inp()
rate = raw_input("Please input your payment rate: ")
try:
    rate = float(rate)
except:
    wrg_inp()


print "Your weekly payment will be C$:",computepay(hours,rate)