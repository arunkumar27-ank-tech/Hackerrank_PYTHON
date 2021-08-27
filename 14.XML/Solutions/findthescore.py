import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
   return sum([len(item.items()) for item in tree.iter()])


xml = input()
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
print(get_attr_number(root))