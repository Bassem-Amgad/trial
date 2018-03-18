import urllib.request
import urllib.parse
import re
url='http://pythonprogramming.net/search'
values={'q':'basic'}

data = urllib.parse.urlencode(values)
data=data.encode('utf=8')
req=urllib.request.Request(url,data)
response=urllib.request.urlopen(req)
#print(response.read())

paragraph=re.findall(r'<p>(.*?)</p>',str(response.read()))
for eachp in paragraph:
     print(eachp)
