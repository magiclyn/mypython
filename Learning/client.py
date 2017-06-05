from socket import * 

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSockt = socket(AF_INET,SOCK_STREAM)
tcpCliSockt.connect(ADDR)
while True:
	data  = input('请输入')
	if not data:
		break
	print(data)
	tcpCliSockt.send(data.encode())
	data = tcpCliSockt.recv(BUFSIZE)

	# print ('data'+data)
	if not data:
		break
	print (data.decode())
tcpCliSockt.close()
