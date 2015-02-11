__author__ = 'Anne'

import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='./xmltmp/aa-driftwood-art.xml')
print (tree.getroot())
root = tree.getroot()
print (root.tag, root.attrib)
print (root[0].tag, root[0].text)
for child_of_root in root:
    print (child_of_root.tag, child_of_root.attrib,child_of_root.text)
for elem in tree.iter():
    #print (elem.tag, elem.attrib,elem.text)
     print ( elem.attrib,elem.text)