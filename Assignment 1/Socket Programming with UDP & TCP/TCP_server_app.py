# Program for TCP server

#import module
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create TCP welcoming socket 
port = 12000
sock.bind(('',port))
sock.listen(1)              # Server begins listening for incoming TCP requests
print ('The server is ready to receive')
while True:
    # server waits on accept() for incoming requests, new socket created on return
    connectSock, addr = sock.accept()       
    # read bytes from socket
    message = connectSock.recv(1024)        
    modifiedMessage = message.decode().upper()      
    connectSock.send(modifiedMessage.encode())

    # close connection to this client 
    connectSock.close()