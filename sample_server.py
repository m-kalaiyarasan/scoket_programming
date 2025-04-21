import socket as s

# print('hello world')

HOST = '0.0.0.0'
PORT = 4568

sck = s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST,PORT))
sck.listen()
print("Waiting for a connection...")
conn,addr = sck.accept()   
conn.sendall("hello, welcome".encode())   # sent a welcome message to the client who conneted to this .
print("Connection recived from {}:{}".format(addr[0],addr[1])) 
data = conn.recv(1024)
while data:
    print(data.decode(), end="")
    data = conn.recv(1024)
    
 