import requests
import urllib3.contrib.pyopenssl

urllib3.contrib.pyopenssl.inject_into_urllib3()
# r = requests.get('https://www.baidu.com',verify = False)
# # print(r.status_code)
# print(r.encoding)
# # print(r.content)
# print(r.headers['content-type'])

# print(type(r.text))
# print(type(r.content))
# # b = r.text.encode("utf-8")
# # print(type(b))
# if False:
# 	r.encoding = 'utf-8'
# 	with open('txt2.html','w',encoding='utf-8') as f:
# 		f.write(r.text)
# else:
# 	with open('txt.html','w',encoding='utf-8') as f:
# 		f.write(r.content.decode('utf-8'))




















# def avg(first,*rest):
# 	print(len(rest))


# def anyargs(f,**kwargs):
# 	keyvals = [' %s="%s"' % item for item in kwargs.items()]
# 	print(keyvals)
# 	print(len(kwargs))


# avg(1,2,3,4,5)


# anyargs(1,a=1,b=3,c=2)