#Full duples

from subprocess import Popen,PIPE,STDOUT
from threading import Thread


def getout(p):
    while p.poll() is None:
        print(p.stdout.readline().decode().strip()) 


p = Popen(['bc','-q'],stdout=PIPE,stdin=PIPE,stderr=STDOUT)

t = Thread(target=getout, args=(p,)).start()

while p.poll() is None:
    inp = input("") + "\n"
    p.stdin.write(inp.encode())
    p.stdin.flush()

    

