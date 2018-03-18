import urllib.request
import urllib.parse

#x= urllib.request.urlopen('http://www.google.com')
#print(x.read())
'''
url='http://pythonprogramming.net/search'
values={'q':'basic'}

data = urllib.parse.urlencode(values)
data=data.encode('utf=8')
req=urllib.request.Request(url,data)
response=urllib.request.urlopen(req)
#print(response.read())
'''
try:
    x=urllib.request.urlopen('http://www.google.com/search/')
    #print(x.read())
except Exception as e:
    print(str(e))

try:
    url=urllib.request.urlopen('http://www.google.com/search/q?test&oq=google&aqs=chrome..69i57j69i60l3j69i65l2.1231j0j1&sourceid=chrome&ie=UTF-8')
    header={}
    header['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'﻿"
    req=urllib.request.Request(url,headers=header)
    response=urllib.request.urlopen(req)
    #print(response.read())

except Exception as e:
    print(str(e))
