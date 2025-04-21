import socket as s

print('hello world')

HOST = '0.0.0.0'
PORT = 4568

sck = s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST,PORT))
sck.listen()
sck.accept()    