d = dict()
# m = list()
fname = raw_input('Enter a file name :')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    # had trouble conceptualizing how to call the second item in the list
    # in order to add it to the dict, decided to assign it to a variable.
    if email in d:
        d[email] += 1
    else:
        d[email] = 1
# make list of values so I can take the max
lst = d.values()
m = max(lst)
# look through all email and compare max to value, print max email, value pair
for address in d:
    if d[address] >= m:
        print address, d[address]