import socket
import os,sys,time

cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Created...")
#
if len(sys.argv)==2 and int(sys.argv[1].split(':')[1])<64000 and int(sys.argv[1].split(':')[1])>1024:
	port=int(sys.argv[1].split(":")[1])
	host=sys.argv[1].split(":")[0]
else:
	port=4444
	host='localhost'
cs.connect((host,port))
print("Connected to port %s"%str(port))
time.sleep(0.2)

def main():
	file_path=input("Enter the file name or full path:")
	file_abspath=os.path.abspath(file_path)
	file_name=os.path.basename(file_path)
	cs.send(file_name.encode('utf8'))

	print("File transfer starting...")
	file=open(file_abspath,'rb')
	
	while True:
		data=file.read(4096)
		if not data: break
		cs.send(data)
		print("Sending...",end="\r")


	cs.close()
	print("Done sending")

main()