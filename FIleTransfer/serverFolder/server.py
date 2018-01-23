import socket
import os,sys

ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=('localhost',4444)
ss.bind(addr)
ss.listen(2)

def main():
    while True:
        try:
            print("server waiting for connection")
            cs,c_addr=ss.accept()
            print("Client connected from:",c_addr)
            file_name=cs.recv(256).decode('utf8')
            print("Reciving file:%s"%file_name)
            #input("Do you want to download it? Press Return to continue or CTRL-D to exit.")
            rcv_file=open(file_name,'wb')
            
            while True:
                data=cs.recv(4096)
                if not data: break
                print("Reciving...",end="\n")
                rcv_file.write(data)


            print("\nRecived")
        except KeyboardInterrupt:
            ss.close()
            sys.exit(1)

    ss.close()

main()

