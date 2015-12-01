fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
somme=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    num=line.lstrip('X-DSPAM-Confidence:')
    num=float(num)
    somme=num+somme
    moy=somme/count
    
print "Average : ", moy