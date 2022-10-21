# Program for TCP client

# import modules
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)     # create TCP socket for server 
address = '172.23.0.209'        # This is system server IP address or server name 
port = 12000        # Remote port 12000

sock.connect((address,port))
message = input('input lowercase sentence: ')

sock.send(message.encode())
modifiedMessage =   sock.recv(1024)         
print('From Server:', modifiedMessage.decode())
sock.close()
