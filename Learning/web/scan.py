#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

# 必须以root权限运行

import socket
import sys
import time
import random

from struct import *

# 计算校验和
def checksum(msg):
    s = 0
    # 每次取2个字节
    for i in range(0,len(msg),2):
        w = (msg[i]) << 8 + (msg[i+1])
        s = s+w

    s = (s>>16) + (s & 0xffff)
    s = ~s & 0xffff

    return s

def CreateSocket(source_ip,dest_ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
    except Exception as msg:
        print ('Socket create error: ',msg)
        sys.exit()

    # 设置手工提供IP头部
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    return s

# 创建IP头部
def CreateIpHeader(source_ip, dest_ip):
    packet = ''

    # ip 头部选项
    headerlen = 5
    version = 4
    tos = 0
    tot_len = 20 + 20
    id = 0#random.randrange(18000,65535,1)
    frag_off = 0
    ttl = 255
    protocol = socket.IPPROTO_TCP
    check = 10
    saddr = socket.inet_aton ( source_ip )
    daddr = socket.inet_aton ( dest_ip )
    hl_version = (version << 4) + headerlen
    ip_header = pack('!BBHHHBBH4s4s', hl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)

    return ip_header

# 创建TCP头部
def create_tcp_syn_header(source_ip, dest_ip, dest_port):
    # tcp 头部选项
    source = random.randint(32000,62000)    # 随机化一个源端口
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

def ByteToHex( bins ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """

    return ''.join( [ "0x%02X " % x for x in bins ] ).strip()
def range_scan(source_ip, dest_ip, start_port, end_port) :
    syn_ack_received = []   # 开放端口存储列表

    for j in range (start_port, end_port) :
        s = CreateSocket(source_ip, dest_ip)
        ip_header = CreateIpHeader(source_ip, dest_ip)
        tcp_header = create_tcp_syn_header(source_ip, dest_ip,j)
        packet = ip_header + tcp_header

        s.sendto(packet, (dest_ip, 0))

        data = s.recvfrom(1024) [0][0:]
        # print(len(data))
        # print(data)

        ip_header_len = (data[0] & 0x0f) * 4
        ip_header_ret = data[0: ip_header_len - 1]
        tcp_header_len = (data[32] & 0xf0)>>2
        tcp_header_ret = data[ip_header_len:ip_header_len+tcp_header_len - 1]

        c = ByteToHex(tcp_header_ret)
        print(c)
        print(tcp_header_ret[0])
        print(tcp_header_ret[1])
        try:
            if tcp_header_ret[13] == 0x12: # SYN/ACK flags 
                syn_ack_received.append(j)
        except Exception as a:
            pass
    return syn_ack_received


# 程序从这里开始:
open_port_list = []
ipsource = '192.168.76.103'
ipdest = '192.168.76.103'
start = 1049
stop = 1052
step = (stop-start)/10
scan_ports_temp = range(start, stop)
scan_ports = []
for a in scan_ports_temp:
	scan_ports.append(a)
if scan_ports[len(scan_ports)-1] < stop:
    scan_ports.append(stop)
for i in range(len(scan_ports)-1):
    opl = range_scan(ipsource, ipdest, scan_ports[i], scan_ports[i+1])
    open_port_list.append(opl)
for i in range(len(open_port_list)):
    print ('Process #: ',i,' Open ports: ',open_port_list[i])
print ('A list of all open ports found: ')
for i in range(len(open_port_list)):
    for j in range(len(open_port_list[i])):
        print (open_port_list[i][j],', ')
