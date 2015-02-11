#from django.test import TestCase
#from django.db import models
from urllib.request import Request, urlopen
from urllib.error import  URLError
import sqlite3
import csv
conn = sqlite3.connect('..\db.sqlite3')
c = conn.cursor()
#c.execute('''CREATE TABLE myList
#             (num , trans text, symbol text, qty real, price real)''')

c.execute('select * from get_img_imagestore')
with open('get_img_imagestore_00.csv', 'w') as fout:
    writer = csv.writer(fout)
    writer.writerow([ i[0] for i in c.description ]) # heading row
    writer.writerows(c.fetchall())
fout.close()


purchases = [(2006, 'BUY', 'IBM', 'fdf', 'sdfs'),
             (2007, 'BUY', 'MSFT', 'asd', 'sadf'),
             (2008, 'SELL', 'IBM', 'sadf', 'asdf'),
            ]
#c.executemany('INSERT INTO myList VALUES (?,?,?,?,?)', purchases)

#conn.commit()
conn.close()

WebList = ('pinterest','flickr','hometalk','diynetwork')
iw=-1
exList = False
url = "www.flickr.com"
for w in WebList:
    iw=url.find(w)
    if (iw!=-1):
        exList=True
print (url,exList)

i=-1
exList = False
url1 = "www.thisisablog.com"
for w in WebList:
    i=url1.find(w)
    if (i!=-1):
        exList=True
print (url1,exList)


someurl = 'http://google.com'
someurl="http://cdn0.notonthehighstreet.com/system/product_images/images/000/646/373/original_noths%252520driftwood%252520beach%252520hut%252520-%252520lge.jpg"
req = Request(someurl)
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    # everything is fine
    print (someurl," opened")




