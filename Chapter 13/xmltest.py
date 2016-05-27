import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_233696.xml'
page = urllib.urlopen(serviceurl)
data = page.read()
tree = ET.fromstring(data)
people = tree.findall('.//name')
count = tree.findall('.//count')
total = 0

#while True:

for numer in count:
    total = total + int(numer.text)
print "Total : ",total