import socket
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
	print("connection error")
host="127.0.0.1"
port=1234
s.bind((host,port))
s.listen(5)
print("Waitinng for clients")
while True:
	clients,addr=s.accept()
	s.send(bytes("connection successfully","utf-8"))
	name=clients.recv(1024).decode()
	print(f"address is:{addr} and client name is:{name}")
	
	#msg=input(">>>")
	
	#clients.send(bytes(msg,"utf-8"))
	#print(clients.recv(1024).decode())
	
	
