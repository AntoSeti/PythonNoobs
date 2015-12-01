x = 'X-DSPAM-Confidence:    0.8475'
print x
pos = x.find(':')
print pos
print x[pos:]
num = float(x[pos+1:])
print num, type(num)

# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname,"r")
for line in fh:
    line=line.rstrip()
    print line.upper()