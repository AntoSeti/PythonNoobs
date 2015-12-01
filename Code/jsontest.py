import json
import urllib

import xml.etree.ElementTree as ET

# url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_200720.json'

input = '''
[
   {
      "name":"Bryson",
      "count":99
    },
    {
      "name":"Curtis",
      "count":98
    },
    {
      "name":"Ainslie",
      "count":98
    },
    {
      "name":"Caydee",
      "count":97
    },
    {
      "name":"Kai",
      "count":95
    },
    {
      "name":"Nuala",
      "count":92
    },
    {
      "name":"Farah",
      "count":89
    },
    {
      "name":"Faryn",
      "count":87
    },
    {
      "name":"Yassin",
      "count":87
    },
    {
      "name":"Salman",
      "count":84
    },
    {
      "name":"Cael",
      "count":84
    },
    {
      "name":"Luka",
      "count":83
    },
    {
      "name":"Natividad",
      "count":83
    },
    {
      "name":"Nikos",
      "count":82
    },
    {
      "name":"Sinai",
      "count":81
    },
    {
      "name":"Diaz",
      "count":81
    },
    {
      "name":"Roslyn",
      "count":80
    },
    {
      "name":"Deborah",
      "count":77
    },
    {
      "name":"Fynn",
      "count":74
    },
    {
      "name":"Andra",
      "count":73
    },
    {
      "name":"Khaela",
      "count":71
    },
    {
      "name":"Enrique",
      "count":70
    },
    {
      "name":"Airlie",
      "count":69
    },
    {
      "name":"Regina",
      "count":69
    },
    {
      "name":"Tayler",
      "count":67
    },
    {
      "name":"Janelle",
      "count":64
    },
    {
      "name":"Lenyn",
      "count":63
    },
    {
      "name":"Marko",
      "count":62
    },
    {
      "name":"Shanice",
      "count":57
    },
    {
      "name":"Becky",
      "count":56
    },
    {
      "name":"Sharland",
      "count":53
    },
    {
      "name":"Peebles",
      "count":53
    },
    {
      "name":"Joe",
      "count":52
    },
    {
      "name":"Maxie",
      "count":51
    },
    {
      "name":"Tammi",
      "count":45
    },
    {
      "name":"Shinade",
      "count":44
    },
    {
      "name":"Mahek",
      "count":43
    },
    {
      "name":"Lida",
      "count":33
    },
    {
      "name":"Simon",
      "count":32
    },
    {
      "name":"Emelye",
      "count":31
    },
    {
      "name":"Bruin",
      "count":30
    },
    {
      "name":"Caitlinn",
      "count":28
    },
    {
      "name":"Sheafan",
      "count":24
    },
    {
      "name":"Lilygrace",
      "count":22
    },
    {
      "name":"Emmanuel",
      "count":19
    },
    {
      "name":"Marion",
      "count":17
    },
    {
      "name":"Aylie",
      "count":10
    },
    {
      "name":"Malakai",
      "count":8
    },
    {
      "name":"Arfa",
      "count":7
    },
    {
      "name":"Blaine",
      "count":4
    }
  ]
'''

# Lecture des donnees
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data

info = json.loads(input)
print 'User count:', len(info)

numlist = list()
for item in info:
    print 'Count :', float(item['count'])
    numlist.append(int(item['count']))
    
print sum(numlist)