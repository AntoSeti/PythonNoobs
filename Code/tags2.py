# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

link = raw_input('Enter - ')
position = int(raw_input("Enter the position:"))
count_ = int(raw_input("Please give me a count:"))

def main(link, position, count_):
    for _ in xrange(count_):
        page = urllib.urlopen(link).read()
        soup = BeautifulSoup(page)
        tags = soup.findAll('a')
        link = tags[position-1].get('href', None)
    return link

#if __name__ == '__main__':
print main(link, position, count_)