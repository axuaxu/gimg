__author__ = 'Anne'

import sqlite3
conn = sqlite3.connect('..\db.sqlite3')
c = conn.cursor()


#c.execute("SELECT * FROM myList " )
#row = c.fetchone()

#print (row)

tline = [(None,2,'http://abcnews.go.com/images/Entertainment/ht_amber_squires_duct_tape_prom_dress_thg_130401_wblog.jpg','http://abcnews.go.com/blogs/entertainment/2013/04/couple-wears-duct-tape-outfits-to-prom','couple wears duct tape outfits to prom','duct tape dress'),
(None,3,'http://bloximages.chicago2.vip.townnews.com/eastvalleytribune.com/content/tncms/assets/v3/editorial/f/e8/fe8371e8-bfa3-11e1-b484-0019bb2963f4/4fe9db28cae0f.image.jpg','http://www.eastvalleytribune.com/local/education/article_cdfb96d6-bfa3-11e1-80d1-0019bb2963f4.html','article_cdfb96d6 bfa3 11e1 80d1 0019bb2963f4.html','duct tape dress'),
(None,4,'https://s-media-cache-ak0.pinimg.com/originals/90/42/10/904210d25eea1adb150938805b30f6b9.jpg','https://www.pinterest.com/explore/duct-tape-dress','duct tape dress','duct tape dress'),
  ]

#c.executemany('INSERT INTO get_img_imagelist VALUES (?,?,?,?,?,?)', tline)
c.execute("upate get_img_imagelist set ImageTitle='<a href=art.org>art</a>' where id=1 " )
#for row in c.execute('SELECT * FROM get_img_imagelist'):
       # print (row)
#print (row)
#with open('mydump.sql', 'w') as f:
#    for line in conn.iterdump():
#        f.write('%s\n' % line)
conn.commit()
conn.close()

while True:
     try:
         x = int(raw_input("Please enter a number: "))
         break
     except ValueError:
         print ("Oops!  That was no valid number.  Try again...")