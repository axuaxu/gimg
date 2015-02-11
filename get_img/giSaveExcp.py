from urllib.request import Request, urlopen
from urllib.error import  URLError,HTTPError
import shutil,sys
from pathlib import Path
import sqlite3
conn = sqlite3.connect('..\db.sqlite3')
c = conn.cursor()

p = Path('.')
FileList = list(p.glob('./tmp/*.*'))
for w in FileList:
    FileName = w.parts[1]
    print (FileName)
    FindDot = FileName.find(r'.')
    inName = r'./tmp/'+FileName
    OutName = r'./output/'+FileName[0:FindDot]+r'.csv'
    ImageKeyword = FileName[0:FindDot]
    inFile = open(inName,'r', encoding='utf8')
    outFile = open(OutName,'w')
    bufferHTML = inFile.read()
    t=0
    tline = ''
    url=''
    i =1

    while (i!=-1):
        i = bufferHTML.find(r'<!--n--><!--m--><div class="rg_di rg_el"')
        l = len(bufferHTML)
        bufferHTML = bufferHTML[i+10:]
        t = t + 1
        i =  bufferHTML.find(r'imgres?imgurl=')
        j = bufferHTML.find('imgrefurl')-1
        url = bufferHTML[i+14:j]

        #<img src="pic_mountain.jpg" alt="Mountain View" style="width:304px;height:228px">
        imageurl = '<img src="'+url+'" style="width:300px">'
        k = bufferHTML.find(r'&h=')
        ref = bufferHTML[j+11:k]
        bufferHTML = bufferHTML[k:]
        if ref.endswith('/'):
             ref= ref[:-1]
        ts = ref.rfind('/')+1
        PageTitle = ref[ts:].replace('-',' ')
        PageTitle = PageTitle.replace('_',' ')
        if (i!=-1):
           #tline = tline + "{"+str(i)+":"+str(t)+":"+url+"\n:"+ref+"\n:"+PageTitle+"\n:"+ImageKeyword+"},\n"
            req = Request(url)
            try:
                response = urlopen(req)
            except HTTPError as e:
                #pass
                print('The server couldn\'t fulfill the request. Error code: ', e.code, url)
            except URLError as e:
                #pass
                if hasattr(e, 'reason'):
                    print('We failed to reach a server.  Reason: ', e.reason, url  )
                elif hasattr(e, 'code'):
                    print('The server couldn\'t fulfill the request.  Error code: ', e.code, url)
            except:
                #pass
                 print ("Unexpected error:", sys.exc_info()[0])
            else:
    # everything is fine
                # print (someurl," opened")
                 oneLine = "("+str(t)+",'"+imageurl+"','"+ref+"','"+PageTitle+"','"+ImageKeyword+"')"
                 insertSQL = "insert into get_img_imagestore (ImageOrder,ImageURL,ImageREF,ImageTitle,ImageKeyword)  values "+oneLine
                 #print(insertSQL)
                 c.execute(insertSQL )
                 tline = tline + oneLine +",\n"

  #print url
    tline = "["+tline+"]"
    outFile.write(tline)
    #print (tline)
    #c.executemany('INSERT INTO get_img_imagestore VALUES (?,?,?,?,?,?)',tline)
    conn.commit()
    outFile.close
    inFile.close


#for row in c.execute('SELECT * FROM get_img_imagestore'):
#        print (row)
conn.close()


for w in FileList:
    FileName = w.parts[1]
    inName = r'./tmp/'+FileName
    destName =  r'./input/'+FileName
    shutil.move(inName, destName)




