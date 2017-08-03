import socket
import os
import struct
# 监听的主机
host = "192.168.76.103"
print(os.name)

# 创建原始套接字，然后绑定在公开接口上
if os.name == "nt":       #windows os.name =nt     windows允许我们嗅探所有协议的所有数据包 LINUX智能嗅探ICMP
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket_protocol)
sniffer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sniffer.bind((host, 0))

# 设置在捕获的数据包中包含IP头
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# 如果在windows下 需要设置IOCTL以启用混杂模式
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

while  True:
	# 读取一个单独的数据包
	packet = sniffer.recvfrom(65565)
	# print (packet)

	packet = packet[0]  
	ip_header = packet[0:20] 
	iph = struct.unpack('!BBHHHBBH4s4s' , ip_header) 

	version_ihl = iph[0] 
	version = version_ihl >> 4 
	ihl = version_ihl & 0xF 
	iph_length = ihl * 4 
	ttl = iph[5] 
	protocol = iph[6] 
	s_addr = socket.inet_ntoa(iph[8]); 
	d_addr = socket.inet_ntoa(iph[9]); 

	tcp_header = packet[20:40]
	tcph = struct.unpack('!HHLLBBHHH',tcp_header)

	s_port = tcph[0]
	d_port = tcph[1]
	# print("fweffffffffffffffffffffff")
	try:

		s_name = socket.gethostbyaddr(s_addr)[0]

	except:
		s_name = ''

	try:

		d_name = socket.gethostbyaddr(d_addr)[0]
	except:
		d_name = ""
	# if 'gongg' in s_name:
		# print(d_port)
		# if d_port == 80 or d_port == 443:
	# if d_port == 8001 or s_port == 8001:
	print(s_addr,s_port)
	print(d_addr,d_port)
	print(s_name)
	print(d_name)
	print(iph[2])
	# print(packet)
	print("----------------------------")



# 在windows下关闭混杂模式
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)