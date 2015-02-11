#parse google image search result, get imgurl,imgrefurl,title
import json
f = open('v01.htm','r+')
o = open('o01.txt','w')
bufferHTML = f.read()

t=1
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
  k = bufferHTML.find(r'&h=')
  ref = bufferHTML[j+11:k]
  bufferHTML = bufferHTML[k:]
  if ref.endswith('/'):
     ref= ref[:-1]
  ts = ref.rfind('/')+1
  PageTitle = ref[ts:].replace('-',' ') 
  if (i!=-1):
      tline = tline + "{"+str(i)+":"+str(t)+":"+url+"\n:"+ref+"\n:"+PageTitle+"},\n"
  
  #print url
tline = "["+tline+"]\n\n" 
o.write(tline)

#json.dumps(tline,o)  
#json.dumps(tline)
o.close
f.close