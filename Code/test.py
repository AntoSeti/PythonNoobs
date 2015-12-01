largest = None
smallest = None

while True:
   
    try:
        num = raw_input("Enter a number: ")
        if num == "done" : break
        
        num = int(num)
        if largest is None: largest=num
        elif num > largest :
            largest=num

        if smallest is None: smallest=num
        elif num < smallest :
            smallest=num
        
    except:
        print "Invalid input"
        continue
      
print "Maximum is", largest
print "Mininum is", smallest
