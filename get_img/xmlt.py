__author__ = 'Anne'
from xml.etree import ElementTree

with open('./xmltmp/aa-driftwood-art.xml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter():
    print (node.tag, node.attrib)
for node in tree.iter('field'):
    name = node.attrib.get('type')
    url = node.attrib.get('pk')

    if name and url:
        print ('  %s :: %s' % (name, url))
    else:
        print (name)