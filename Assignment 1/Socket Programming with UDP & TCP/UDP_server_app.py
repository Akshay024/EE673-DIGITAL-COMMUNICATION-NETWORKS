# Program for UDP Server 

# import module
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # Create UDP socket     
port = 12000                  
# address = '172.23.0.209'        # System's IP address 

sock.bind(('',port))         # Bind socket to local port number 12000
    
print ('The server is ready to receive')
while True:
    # Read from UDP socket into message, getting client's address 
    message, clientAddress = sock.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    # send uppercase letter back to string
    sock.sendto(modifiedMessage.encode(),  clientAddress)