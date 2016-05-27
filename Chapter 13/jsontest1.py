import json
import urllib

page_address = urllib.urlopen("http://python-data.dr-chuck.net/comments_233700.json").read()

json_content = json.loads(page_address)
total = 0

i = 0
for values in json_content['comments']:
	#print json_content['comments'][i]['count']
	total = total + json_content['comments'][i]['count']
	i = i + 1
print 'Total sum: ',total