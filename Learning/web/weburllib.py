from urllib import request
response = request.urlopen('http://python.org')
page = response.read()

print(page)