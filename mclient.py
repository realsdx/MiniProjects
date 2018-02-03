import socket
import struct
import threading

MCAST_GRP='225.0.0.5'
MCAST_PORT=55777
MADDR=(MCAST_GRP,MCAST_PORT)

ms=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ms.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,1)
ms.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ms.bind(('',MCAST_PORT))
ms.settimeout(100)
grp=socket.inet_aton(MCAST_GRP)
mreq=grp + struct.pack('=I',socket.INADDR_ANY)
ms.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
print("CLIENT SETUP COMPLETE")

def receive():
	while True:
	    data,sender=ms.recvfrom(4096)
	    print("\r{}-said:{}".format(sender,data.decode('UTF-8')))

def send():
	while True:
	    msg=input("<YOU-->").encode("UTF-8")
	    ms.sendto(msg,MADDR)

t1=threading.Thread(target=receive)
t2=threading.Thread(target=send)

t2.start()
t1.start()

t1.join()
t2.join()

ms.close()
print("socket closed")
