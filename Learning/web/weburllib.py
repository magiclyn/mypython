from urllib import request
import urllib.parse

import socket
import urllib.error
import urllib.request

response = request.urlopen('http://www.python.org')
page = response.read()
page = page.decode('utf-8')
# print(page)

print(type(response))

print(response.status)

a = response.getheaders()
print(type(a))

print(response.getheaders())

print(response.getheader('server'))



data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding = 'utf-8')
response = request.urlopen('http://httpbin.org/post',data = data)
print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')