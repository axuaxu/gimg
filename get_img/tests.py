#from django.test import TestCase
import shutil
from pathlib import Path
# Create your tests here.
a="adsfakdsj.mkdk"
i0 =a.find(r'.')
b= a[0:i0]
print(b)

p = Path('.')
FileList = list(p.glob('./tmp/*.html'))
for w in FileList:
    FileName = w.parts[1]
    #print(w)
    print (FileName)
    FindDot = FileName.find(r'.')
    inName = r'./tmp/'+FileName
    destName =  r'./input/'+FileName
    OutName = r'./output/'+FileName[0:FindDot]+r'.csv'
    inFile = open(inName,'r+',encoding='utf8')
    bufferHTML = inFile.read()
    outFile = open(OutName,'w')
    OutName = r'./output/'+b+r'.csv'
    outFile = open(OutName,'w')
    inFile.close
    outFile.close

for w in FileList:
    FileName = w.parts[1]
    inName = r'./tmp/'+FileName
    destName =  r'./input/'+FileName
    shutil.move(inName, destName)