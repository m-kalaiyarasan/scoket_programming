#half duples

from subprocess import Popen,PIPE,STDOUT

p = Popen(['bc','-q'],stdout=PIPE,stdin=PIPE,stderr=STDOUT)

while p.poll() is None:
    inp = input(" ") + "\n"
    p.stdin.write(inp.encode())
    p.stdin.flush()
    print(p.stdout.readline().decode().strip())  # remove the "\n" from the output.
    

#  this half duples will only print one output for one input, so if we run for loop, 
#  it only print the first value and balance are in queue as buffer
#  use thread to manage automatically print the STDOUT pipi whatever Data comes

#half duples, recive or send, cant do both 