import codecs
import re
import locale

ENCODING_RE = re.compile(b'coding[:=]\s*([-\w.]+)')

f1 = open('nobomutf8.txt','r',encoding='utf-8')
s1 = f1.read()
print(s1)
f1.close()


f8 = open('nobomutf8.txt','rb')
sf8 = f8.read()
print("-------------------------------")
# for line in sf8.split(b'\n')[:2]:
#     if line[0:1] == b'#' and ENCODING_RE.search(line):
#         encoding = ENCODING_RE.search(line).groups()[0].decode('ascii')
#         print("encoding:%s" % encoding)
#         print(data.decode(encoding))
# print(sf8.decode(locale.getpreferredencoding(False)))
strf8 = sf8.decode('utf-8')
print(strf8)
f8.close()

print("-------------------------------")

f2 = open('utf8.txt','r',encoding='utf-8-sig')
s2 = f2.read()

lines = enumerate(s2.splitlines(),start = 1)

print(s2)
f2.close()


fb = open('utf8.txt','rb')
sfb = fb.read()
a = sfb.startswith(codecs.BOM_UTF8)

strsb = sfb[len(codecs.BOM_UTF8):].decode('utf-8')
fb.close()
print(a)
print(strsb)

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


