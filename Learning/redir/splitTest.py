import re

str = 'href="images/img_2.jpg"'

pattemImage = re.compile('href="images/(.*)jpg"')

replaceList = ('href="(images/.*?)"','img src="(images/.*?)"','src="(js/.*?)"','href="(css/.*?)"')

data = ''

htmlname = 'pricing.html'
with open(htmlname,'r+',encoding='utf-8') as f:
	data = f.read()
	for pattem in replaceList:
		

		m = re.findall(pattem,data,re.M)
		print(m)

		if m != None:
			for  s in m:
				temp = "{{% static '{}'%}}"
				temp = temp.format(s)
				print(temp)
				data = data.replace(s,temp)
				# data = re.sub(s,temp,data)
		# print(data)
	# f.write(data)

with open(htmlname,'w',encoding='utf-8') as f:
	f.write(data)

# temp = "{{% static '{}'%}}"

# print(temp.format('images/img_3.jpg'))
# S = '123,432'

# N = RE.SUB('2','XXX',S)
# PRINT(N)



# {% static 'images/img_3.jpg'%}
	# a = pattemImage.split(data)
	# print(len(a))

	# for i in range(len(a)):
	# 	temp = a[i]

	# print(data)
	# print(type(data))
	# print(len(data))
	# allfind = re.findall('div',data)
	# # print(allfind)
	# alllist = pattemImage.search(data)
	# print(alllist.group())

	# allmatch = pattemImage.match(str)
	# print(allmatch)

# p = re.compile('(\d+)')
# str = '123abc3cc4sdfc'

# a = p.split(str)
# print(a)

# b = ''.join(a)
# print(b)

# for i in a:
# 	m = re.match('\d+',i)
# 	if m == None:
# 		print('none %s'%i)
# 	else:
# 		print('not none')