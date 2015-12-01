import re

fhandle = open("regex_sum_200714.txt")

numlist = list()
for line in fhandle:
	line = line.rstrip()
	num = re.findall('[0-9]+', line)
	print num
	if len(num) > 0:
		for number in num:
		    numlist.append(float(number))
		
print numlist
print len(numlist)
print sum(numlist)
	# numlist.append(number)
		