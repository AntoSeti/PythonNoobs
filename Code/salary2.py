hours=raw_input('Enter hours : ')
rate=raw_input('Enter Rate : ')
try:
    hours=float(hours)
    rate=float(rate)
except:
    print "Error. Idiot, please enter numeric value !"
    quit()
    
print hours
print rate
if hours<=40:
    print hours*rate
else:
    hoursup=hours-40
    ratesup=rate*1.5
    print 40*rate + hoursup*ratesup

