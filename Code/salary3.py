def computepay(hours, rate):
    try:
        hours=float(hours)
        rate=float(rate)
    except:
        print "Error. Idiot, please enter numeric value !"
        quit()
    
# print hours, rate

    if hours<=40:
        print hours*rate
    else:
        hoursup=hours-40
        ratesup=rate*1.5
        print 40*rate + hoursup*ratesup
    
computepay(45, 10)

