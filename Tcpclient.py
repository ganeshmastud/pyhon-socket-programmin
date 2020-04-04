import socket
try:
	client_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
	print("connection error")
client_s.connect(("127.0.0.1",1234))
cmsg=""

name=input("Enter your name:>\t")
while True:
	print(client_s.recv(1024).decode())
	
	client_s.send(bytes(name,"utf-8"))
	#send_msg=input(f"{name}>>>")
	
	
	
	#client_s.send(bytes(send_msg,"utf-8"))
	#another way
	#msg=client_s.recv(8)
	#if not len(msg):
		#print("hello")
	#	break
	#cmsg +=msg.decode("utf-8")
	#print(cmsg)
#print(cmsg)#statment can't reach