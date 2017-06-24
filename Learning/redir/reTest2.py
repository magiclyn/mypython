import re

str = 'vbaaabbcdeeefaabc'

n = re.match('a.*?b(\w?)',str)
m = re.search('a.*?b(\w?)',str)

print(m) 
print(m.group())
print(m.groups())
print(m.span())
print(len(m.groups()))


str2 = 'theab theac'

l = re.findall('((the)a\w)',str2)

print(l)