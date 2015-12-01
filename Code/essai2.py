fname = raw_input("Enter file name: ")
fh = open(fname)
words = list()

for line in fh:
	line = line.rstrip()
	line = line.split()
    
	for word in line :
        	if word in words : continue
        	else : words.append(word)

words.sort()
print words


fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

count = 0
for line in fh:
    if line.startswith('From '):
        count = count + 1
        ln = line.split()
        print ln[1]

print "There were", count, "lines in the file with From as the first word"