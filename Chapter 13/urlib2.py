import urllib
from BeautifulSoup import *

position = int(raw_input("Position: "))
count = int(raw_input("Count: "))


url = "http://python-data.dr-chuck.net/known_by_Iiona.html"

while count > 0:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	urls = []
	names = []

	for tag in tags:
		urls.append(tag.get('href'))
		names.append(tag.contents[0])
		#print urls
		
	count = count - 1	
	url = urls[position-1]
	name = names[position-1]
	#print url
	print name