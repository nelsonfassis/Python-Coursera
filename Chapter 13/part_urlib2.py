import urllib
from BeautifulSoup import *

#position = int(raw_input("Position: "))
#count = int(raw_input("Count: "))
urls = []

url = "http://python-data.dr-chuck.net/known_by_Fikret.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')


for line in soup:
	print line

'''

while count > 0:
	for tag in tags:
		urls.append(tag.get('href'))
		#print urls
		count = count - 1

	url = urls[position-1]
	print url

'''