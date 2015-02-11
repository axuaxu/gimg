__author__ = 'Anne'
import sqlite3
from random import randint
from time import strftime


TimeNow = strftime("%Y-%m-%d %H:%M:%S")
NowStr = TimeNow[:10].replace('-','/')
print (TimeNow,TimeNow[:10],NowStr)

tis = '1234567901234567901234567890'
print (tis[0:50]+'.jpg')
sty = "this is .html.dsfkj.df"
t = sty.rfind('.')
substy = sty[:t]
print (substy)
conn = sqlite3.connect('..\db.sqlite3')
c = conn.cursor()

#c.execute("delete FROM get_img_imagestore " )
c.execute("select * FROM get_img_amazon " )
all_rows = c.fetchall()
conn.commit()
conn.close()
#print('1):', all_rows)
rCount =  len(all_rows)
print (rCount)
randCt1 = randint(1,rCount)
randCt2 = randint(1,rCount)
randCt3 = randint(1,rCount)
amazonLink = ''
iCt = 0;
for row in all_rows:
    # row['name'] returns the name column in the query, row['email'] returns email column.
    iCt = iCt + 1
    if (iCt == randCt1) or (iCt == randCt2) or (iCt == randCt3):
        #print(iCt,row[1],row[2])
        amazonLink  = amazonLink + r'[CBC_AMAZON asin="' +row[1] + ']' + row[2].lstrip(' ')+ '[/CBC_AMAZON]'
        print (amazonLink)


rInt = randint(1,6)
for i in range(35):
   if (rInt+i)%6 ==0:
        pass
        #print (rInt, ' ',i,' ')
t = 'asdsdf.fsfadfasdf.jpg'
m = t[:-5].find('.')
mt = t.split('.')
print (t.split('.')[-1])

print (strftime("%Y-%m-%d %H:%M:%S"))

d = {'name': 'ImageOrder', 'type': 'IntegerField'}

print (d['name'])
if d['name']=='ImageOrder':
    print ('order')
d = {'name': 'ImageOrder', 'type': 'IntegerField'}
try:
  print (d['dfff'])
except KeyError:
  print ('no dfff')
#c.execu te("SELECT * FROM myList " )
