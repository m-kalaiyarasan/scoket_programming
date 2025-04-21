import socket as s
from threading import Thread
import mimetypes as ty

HOST = '0.0.0.0'
PORT = 4558

Http_resp_temp = """
HTTP/1.1 200 OK
Content-Type: {type}
Content-Length: {length}

{body}
"""

class ConnectionThread(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print("Thread {}:{} Started".format(addr[0],addr[1]))
    def run(self):
       
        data = self.conn.recv(1024)
        path='htdocs/'
        file = data.decode()
        file = file.split(" ")[1]
        if(file == "/"):
            file = 'index.html'
        file1 = path+file
        # print(file)
        with open(file1, 'r') as fi:
            body = fi.read()            
        # print(ty.guess_type(file)[0])
        self.conn.sendall(Http_resp_temp.format(type=ty.guess_type(file)[0],length = len(body)+50,body = body).encode())
        # while data:
            
        #     print("{}: ".format(self.addr[0]) + data.decode(), end="")
        #     data = self.conn.recv(1024)
            

sck = s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST,PORT))
sck.listen()

while True:
    print("Waiting for a connection...")
    conn,addr = sck.accept()
    print("Connection recived from {}:{}".format(addr[0],addr[1]))
    
    ConnectionThread(conn,addr).start()
        
 