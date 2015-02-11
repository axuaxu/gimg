__author__ = 'Anne'
import shutil,sys
import xml.etree.cElementTree as ET
from time import strftime
from pathlib import Path

TimeNow = strftime("%Y-%m-%d %H:%M:%S")

tFileName = r'./xmlin/guru-start.xml'
tFile = open(tFileName,'r', encoding='utf8')
StartStr = tFile.read()
tFile.close()
tFileName = r'./xmlin/guru-end.xml'
tFile = open(tFileName,'r', encoding='utf8')
EndStr = tFile.read()
tFile.close()

TitleStr = 'driftwood art'
LinkStr = 'http://www.gurukoala.com/2015/02/03/18-creative-home-decorating-ideas-budget'
PubDate = TimeNow
guidStr = 'http://www.gurukoala.com/?p=425'
imgDir = 'http://gurukoala.com/wp-content/uploads/2015/02/'

ItemStr = '<item>\n<title>' + TitleStr  + '</title>\n'
ItemStr = ItemStr + '<link>' + LinkStr + '</link>\n'
ItemStr = ItemStr + '<pubDate>' + PubDate + '</pubDate>\n'
ItemStr = ItemStr + '<dc:creator><![CDATA[guru]]></dc:creator>\n'
ItemStr = ItemStr + '<guid isPermaLink="false">' + guidStr + '</guid>\n'
ItemStr = ItemStr + '<description></description>\n<content:encoded>\n<![CDATA['


p = Path('.')
FileList = list(p.glob('./xmltmp/*.*'))
allXML = ''
imgCSV = ''
for w in FileList:
    FileName = w.parts[1]
    print (FileName)
    FindDot = FileName.find(r'.')
    inName = r'./xmltmp/'+FileName
    OutName = r'./xmlout/guru-'+FileName[0:FindDot]+r'.xml'
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



    tree = ET.ElementTree(file=inName)
    for elem in tree.iter():
          eName =   elem.attrib
          try:
              if eName['model'] == 'get_img.imageselected':
                 if t>0:
                     imgType = ImageURL.split('.')[-1]
                     localName = ImageTitle.replace(' ','-') + '-' + str(t) + '.' + imgType
                     localURL = imgDir + localName
                     itemHTML = itemHTML+'\n<b>'+str(t)+'. '+ImageTitle.title() +'</b>\n'+'<img style="width: 450px;" src="'
                     #itemHTML = itemHTML+ImageURL +'"alt="" />\n <a href="'+ImageREF+'" target="_blank">source</a>\n'
                     itemHTML = itemHTML+localURL +'"alt="" />\n <a href="'+ImageREF+'" target="_blank">source</a>\n'
                     #amazon
                     if (rInt+t)%6 ==0:
                         amazon = ''
                         itemHTML = itemHTML + amazon
                     imgCSV = imgCSV + ImageURL + ',' + localName + '\n'
                 t = t + 1
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


          print (t,ImageTitle,ImageURL,ImageREF)

    EndItem = ']]></content:encoded>\n<excerpt:encoded><![CDATA[]]></excerpt:encoded>\n'
    EndItem = EndItem + '<wp:post_id>425</wp:post_id>\n<wp:post_date>'+TimeNow+'</wp:post_date>\n'
    EndItem = EndItem + '<wp:post_date_gmt>'+ TimeNow +'</wp:post_date_gmt>\n'
    EndItem = EndItem +	'<wp:comment_status>open</wp:comment_status>\n'
    EndItem = EndItem + '<wp:ping_status>open</wp:ping_status>\n'
    EndItem = EndItem + '<wp:post_name>18-creative-home-decorating-ideas-budget</wp:post_name>\n'
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

tmpTime = TimeNow.replace(' ','-')
tmpTime = tmpTime.replace(':','-')
imgList = r'./xmlout/guru-imglist-'+tmpTime+r'.csv'
allName = r'./xmlout/guru-all-'+tmpTime +r'.xml'

imgFile = open(imgList,'w')
imgFile.write(imgCSV)
imgFile.close()
allFile = open(allName,'w')
allXML = StartStr+allXML+EndStr
allFile.write(allXML)
allFile.close()
