import urllib
from BeautifulSoup import *

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_200719.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
numlist = list()
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('comments', None)
   print 'Contents:',tag.contents[0]
   numlist.append(int(tag.contents[0]))
print numlist
   #print 'Attrs:',tag.attrs
print sum(numlist)
# print sum(float(tag.contents))