from socket import * 
from time import ctime

HOST = '192.168.76.103' #'192.168.76.103'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
print('sdfsdfsdfs')
ss = socket(AF_INET,SOCK_STREAM)
ss.bind(ADDR)
ss.listen(5)
print('sdfsdfsdfs')
while True:
	print ('wait for connection')
	tcpClient,addr = ss.accept()
	print ('....connected from:',addr)

	while  True:
		data = tcpClient.recv(BUFSIZE)
		print(data.decode())
		if not data:
			break
		tcpClient.send(('[%s] %s' % (ctime(),data)).encode())
		# tcpClient.send('[%s] %s' % (ctime(),data))
	tcpClient.close()
ss.close()