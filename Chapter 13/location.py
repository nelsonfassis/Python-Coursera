import json
import urllib

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
address = raw_input('Enter location: ') #"Spiru Haret University" 
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
data = urllib.urlopen(url).read()
js = json.loads(data)
print url
print js['results'][0]['place_id']
