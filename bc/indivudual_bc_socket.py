#Full duples

from subprocess import Popen,PIPE,STDOUT
from threading import Thread
import socket as s

class ProcessOutputThread(Thread):
    def __init__(self,p,conn):
        Thread.__init__(self)
        self.p = p
        self.conn = conn
    def run(self):
        while self.p.poll() is None:
            # print(self.p.stdout.readline().decode().strip())
            # self.conn.sendall("45".encode())
            self.conn.sendall(self.p.stdout.readline())
 
class MathServerThread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
    
    def run(self):
        p = Popen(['bc'],stdout=PIPE,stdin=PIPE,stderr=STDOUT)
        out_t = ProcessOutputThread(p,self.conn)
        out_t.start()
        while p.poll() is None:
            inp = self.conn.recv(1024).decode().strip()
            # print(inp)
            if not inp:
                break
            elif inp == "exit" or inp == "quit":
                print("exit")
                p.kill()
                break
                self.conn.close()
            
            inp = inp + "\n"
            p.stdin.write(inp.encode())
            p.stdin.flush()
            # print("hello")
            # print(p.stdout.readline().decode())

HOST = ''
PORT = 3546

sck = s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST,PORT))
sck.listen()

while True:
    conn, addr = sck.accept()
    t = MathServerThread(conn,addr)
    t.start()
    

