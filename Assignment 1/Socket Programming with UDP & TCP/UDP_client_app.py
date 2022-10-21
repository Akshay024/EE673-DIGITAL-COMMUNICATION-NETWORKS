# Program for UDP client
#import modules 
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #   Create UDP scoket for server
address = '172.23.0.209'        # IP address of system 
port = 12000

print("Ping server ready on port", port)

message = input('input lowercase sentence: ')

sock.sendto(message.encode(), (address,port))   #   send into socket 
modifiedMessage, serverAddress =   sock.recvfrom(2048)  # read reply char from socket into string 
print(modifiedMessage.decode()) # print recieved string

sock.close() # Close socket




