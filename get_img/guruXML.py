__author__ = 'Anne'
import shutil,sys
import xml.etree.cElementTree as ET
import sqlite3
from time import strftime
from pathlib import Path
from random import randint

TimeNow = strftime("%Y-%m-%d %H:%M:%S")
tmpTime = TimeNow.replace(' ','-')
tmpTime = tmpTime.replace(':','-')
NowStr = TimeNow[:10].replace('-','/')
#build amazon link
conn = sqlite3.connect('..\db.sqlite3')
c = conn.cursor()
c.execute("select * FROM get_img_amazon " )
all_rows = c.fetchall()
rCount =  len(all_rows)
conn.commit()
conn.close()
randCt1 = randint(1,rCount)
randCt2 = randint(1,rCount)
randCt3 = randint(1,rCount)
amazonLink = ''
iCt = 0;

tFileName = r'./xmlin/guru-start.xml'
tFile = open(tFileName,'r', encoding='utf8')
StartStr = tFile.read()
tFile.close()
tFileName = r'./xmlin/guru-end.xml'
tFile = open(tFileName,'r', encoding='utf8')
EndStr = tFile.read()
tFile.close()



imgDir = 'http://gurukoala.com/wp-content/uploads/2015/img01/'


p = Path('.')
FileList = list(p.glob('./xmltmp/*.*'))
allXML = ''
imgCSV = ''
for w in FileList:
    FileName = w.parts[1]
    print (FileName)
    FindDot = FileName.find(r'.')
    inName = r'./xmltmp/'+FileName
    OutName = r'./xmlout/guru-'+FileName[0:FindDot]+'-'+tmpTime+r'.xml'
    ImageKeyword = FileName[0:FindDot]
    inFile = open(inName,'r', encoding='utf8')
    outFile = open(OutName,'w')
    bufferXML = inFile.read()
    t=0
    tline = ''
    url=''
    i =1
    ImageTitle=''
    ImageURL=''
    ImageREF=''
    ImageKeyword=''
    itemHTML=''
    rInt = randint(1,6)
    amazon = ''

    TitleStr = FileName[0:FindDot]
    LinkStr = 'http://www.gurukoala.com/'+NowStr+'/'+TitleStr
    PubDate = TimeNow
    guidStr = 'http://www.gurukoala.com/?p=425'
    ItemStr = '<item>\n<title>' + TitleStr  + '</title>\n'
    ItemStr = ItemStr + '<link>' + LinkStr + '</link>\n'
    ItemStr = ItemStr + '<pubDate>' + PubDate + '</pubDate>\n'
    ItemStr = ItemStr + '<dc:creator><![CDATA[guru]]></dc:creator>\n'
    ItemStr = ItemStr + '<guid isPermaLink="false">' + guidStr + '</guid>\n'
    ItemStr = ItemStr + '<description>'+TitleStr+'</description>\n<content:encoded>\n<![CDATA['

    tree = ET.ElementTree(file=inName)
    for elem in tree.iter():
          eName =   elem.attrib
          try:
              if eName['model'] == 'get_img.imageselected':
                 if t>0:
                     imgType = ImageURL.split('.')[-1]
                     ImageTitle = ImageTitle.replace('.',' ')
                     ImageTitle = ImageTitle.replace('-',' ')
                     localName = ImageTitle.replace(' ','-') + '-' + str(t) + '.' + imgType
                     localName = localName.replace('/','-')[0:50]
                     localURL = imgDir + localName
                     itemHTML = itemHTML+'\n<b>'+str(t)+'. '+ImageTitle.title() +'</b>\n'+'<img style="width: 450px;" src="'
                     #itemHTML = itemHTML+ImageURL +'"alt="" />\n <a href="'+ImageREF+'" target="_blank">source</a>\n'
                     itemHTML = itemHTML+localURL +'"alt="" />\n <a href="'+ImageREF+'" target="_blank">source</a>\n'
                     #amazon
                     if (rInt+t)%6 ==0:
                         randCt1 = randint(1,rCount)
                         randCt2 = randint(1,rCount)
                         randCt3 = randint(1,rCount)
                         amazonLink = ''
                         iCt = 0;
                         for row in all_rows:
                              iCt = iCt + 1
                              if (iCt == randCt1) or (iCt == randCt2) or (iCt == randCt3):
                                 amazonLink  = amazonLink + r'[CBC_AMAZON asin="' +row[1].lstrip() + r'"]' + row[2].lstrip(' ')+ '[/CBC_AMAZON]    '
                                 print (amazonLink)
                         itemHTML = itemHTML + '\n' + amazonLink + '\n'
                     imgCSV = imgCSV + ImageURL + ',' + localName + '\n'
                 t = t + 1
                 print (t,ImageTitle,ImageURL,ImageREF)
          except KeyError:
               pass
          try:
              if eName['name'] == 'ImageURL':
                 ImageURL = elem.text
          except KeyError:
               pass
          try:
              if eName['name'] == 'ImageREF':
                 ImageREF = elem.text
          except KeyError:
               pass
          try:
              if eName['name'] == 'ImageTitle':
                 ImageTitle = elem.text
          except KeyError:
               pass
          try:
              if eName['name'] == 'ImageKeyword':
                 ImageKeyword = elem.text

          except KeyError:
               pass


          #print (t,ImageTitle,ImageURL,ImageREF)

    EndItem = ']]></content:encoded>\n<excerpt:encoded><![CDATA[]]></excerpt:encoded>\n'
    EndItem = EndItem + '<wp:post_id>425</wp:post_id>\n<wp:post_date>'+TimeNow+'</wp:post_date>\n'
    EndItem = EndItem + '<wp:post_date_gmt>'+ TimeNow +'</wp:post_date_gmt>\n'
    EndItem = EndItem +	'<wp:comment_status>open</wp:comment_status>\n'
    EndItem = EndItem + '<wp:ping_status>open</wp:ping_status>\n'
    EndItem = EndItem + '<wp:post_name>'+TitleStr+'</wp:post_name>\n'
    EndItem = EndItem + '<wp:status>publish</wp:status>\n'
    EndItem = EndItem + '<wp:post_parent>0</wp:post_parent>\n<wp:menu_order>0</wp:menu_order>\n'
    EndItem = EndItem + '<wp:post_type>post</wp:post_type>\n<wp:post_password></wp:post_password>\n'
    EndItem = EndItem + '<wp:is_sticky>0</wp:is_sticky>\n'
    EndItem = EndItem + '<category domain="post_tag" nicename="budget-home-decor"><![CDATA[budget home decor]]></category>\n'
    EndItem = EndItem + '<category domain="post_tag" nicename="creative-home-decor"><![CDATA[creative home decor]]></category>\n'
    EndItem = EndItem + '<category domain="category" nicename="craft"><![CDATA[DIY Craft]]></category>\n'
    EndItem = EndItem + '<category domain="category" nicename="garden-2"><![CDATA[Garden]]></category>\n'
    EndItem = EndItem + '<category domain="category" nicename="home-decor"><![CDATA[Home Decor]]></category>\n</item>\n'


    allXML = ItemStr+itemHTML+EndItem
    tline = StartStr+ItemStr+itemHTML+EndItem+EndStr
    outFile.write(tline)
    #print (tline)
    #c.executemany('INSERT INTO get_img_imagestore VALUES (?,?,?,?,?,?)',tline)
    outFile.close
    inFile.close


imgList = r'./xmlout/guru-imglist-'+tmpTime+r'.csv'
allName = r'./xmlout/guru-all-'+tmpTime +r'.xml'

imgFile = open(imgList,'w')
imgFile.write(imgCSV)
imgFile.close()
allFile = open(allName,'w')
allXML = StartStr+allXML+EndStr
allFile.write(allXML)
allFile.close()

#for w in FileList:
#    FileName = w.parts[1]
#    inName = r'./xmltmp/'+FileName
#    destName =  r'./xmlbak/'+FileName
#    shutil.move(inName, destName)
