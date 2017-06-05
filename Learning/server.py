from socket import * 
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

ss = socket(AF_INET,SOCK_STREAM)
ss.bind(ADDR)
ss.listen(5)
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