import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
html = urllib.urlopen("http://python-data.dr-chuck.net/comments_233699.html").read()

soup = BeautifulSoup(html)
total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    total = total + int(tag.contents[0])
    print 'Contents:',tag.contents[0]
    print total
    ''''
    print tags
    print tag.find(tags)
 	print 'TAG:',tag
 	print 'URL:',tag.get('href', None)
 
    print 'Attrs:',tag.attrs
    '''