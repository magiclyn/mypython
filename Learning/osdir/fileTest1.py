# import codecs
f1 = open('nobomutf8.txt','r',encoding='utf-8')
s1 = f1.read()
print(s1)
f1.close()

f2 = open('utf8.txt','r',encoding='utf-8-sig')
s2 = f2.read()
print(s2)
f2.close()

f3 = open('unicodebe.txt','r',encoding='utf-16')
s3 = f3.read()
print(s3)
f3.close()

f4 = open('unicodele.txt','r',encoding='utf-16')
s4 = f4.read()
print(s4)
f4.close()

f5= open('ansi.txt','r')# 或encoding='gbk'
s5 = f5.read()
print(s5)
f5.close()


