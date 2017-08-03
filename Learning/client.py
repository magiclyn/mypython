from socket import * 
import pinject

HOST = '192.168.76.103'
Dest = '192.168.76.103'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

# tcpCliSockt = socket(AF_INET,SOCK_STREAM)
# # tcpCliSockt = socket(AF_INET,SOCK_RAW,IPPROTO_RAW)  
# # tcpCliSockt.setsockopt(IPPROTO_IP,IP_HDRINCL,1)     
# # tcpCliSockt.setsockopt(SOL_SOCKET,SO_SNDTIMEO,2000)
# tcpCliSockt.connect(ADDR)
# while True:
# 	data  = input('请输入')
# 	if not data:
# 		break
# 	print(data)
# 	tcpCliSockt.send(data.encode())
# 	data = tcpCliSockt.recv(BUFSIZE)

# 	# print ('data'+data)
# 	if not data:
# 		break
# 	print (data.decode())
# tcpCliSockt.close()



try:
	s = socket(AF_INET, SOCK_RAW)
	s.setsockopt(IPPROTO_IP,IP_HDRINCL,1)
	# s.connect(ADDR)
except Exception as e:
	print ('Socket could not be created. Error Code : ' ,e)

ip = pinject.IP(HOST,Dest,'',IPPROTO_UDP)

ip_head = ip.pack()
print(ip_head)
# print(type(ip_head))
print(len(ip_head))

# tcp = pinject.TCP(PORT,PORT)
udp = pinject.UDP(PORT,PORT)

# h = inet_aton(HOST)
# he = inet_aton(Dest)
# type(h)
# print(h)
# print(len(h))
# tcp_head = tcp.pack(h,he)
udp_head = udp.pack(HOST,Dest)


word = '1'.encode()

a = ip_head+udp_head+word
print(len(a))
print(ADDR)
s.sendto(a,ADDR)

# data = s.recvfrom(1024) [0][0:]

# ipbytes = data[0:20]



# ip_head2 = ip.unpack(ipbytes)
# print(ip_head2.list)






def create_tcp_syn_header(source_ip, dest_ip, dest_port):  
    # tcp 头部选项  
    source = random.randrange(32000,62000,1)    # 随机化一个源端口  
    seq = 0 
    ack_seq = 0 
    doff = 5 
    # tcp flags  
    fin = 0 
    syn = 1 
    rst = 0 
    psh = 0 
    ack = 0 
    urg = 0 
    window = socket.htons (8192)    # 最大窗口大小  
    check = 0 
    urg_ptr = 0 
    offset_res = (doff << 4) + 0 
    tcp_flags = fin + (syn<<1) + (rst<<2) + (psh<<3) + (ack<<4) + (urg<<5)  
    tcp_header = pack('!HHLLBBHHH', source, dest_port, seq, ack_seq, offset_res, tcp_flags, window, check, urg_ptr)  
    # 伪头部选项  
    source_address = socket.inet_aton( source_ip )  
    dest_address = socket.inet_aton( dest_ip )  
    placeholder = 0 
    protocol = socket.IPPROTO_TCP  
    tcp_length = len(tcp_header)  
    psh = pack('!4s4sBBH', source_address, dest_address, placeholder, protocol, tcp_length);  
    psh = psh + tcp_header;  
    tcp_checksum = checksum(psh)  
 
    # 重新打包TCP头部，并填充正确地校验和  
    tcp_header = pack('!HHLLBBHHH', source, dest_port, seq, ack_seq, offset_res, tcp_flags, window, tcp_checksum, urg_ptr)  
    return tcp_header  