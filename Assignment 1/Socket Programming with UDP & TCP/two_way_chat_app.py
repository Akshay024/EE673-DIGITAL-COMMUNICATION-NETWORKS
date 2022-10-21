## Program for UDP chat application for communicating with phone using the UDP monitor 

# This library is for Text
from pyfiglet import Figlet

title = Figlet(font='puffy').renderText("Two way Chat App with UDP monitor")
print(title)

# import modules
import socket
import sys
import threading


#Function for sending message
def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Good to see you"
    while True:
        if "exit" in message or "end" in message:   #If user types exit or end then the program will terminate and close the application from user side.
            exit()
        else:
            message = input()
            message = username+":"+ message         # On UDP monitor message appears as 'Godspeed:message'
            sock.sendto(message.encode(), (IP4_receiver, Port_receiver))
            
# Function for receiving message
def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP4_client, Port_client)) # binding the IP address and port number
    while True:
        message = sock.recvfrom(1024)
        print("UDP Monitor: "+message[0].decode())   # Our system message appears as 'UDP Monitor: message'
        if "exit" in message[0].decode() or "end" in message[0].decode():  # if receiver types exit or end the program will terminate from his side
            sys.exit()

print("Here we go....")
IP4_receiver = input("\nEnter the IP address of reciever: ")   # for me its 172.23.3.116
Port_receiver = int(input("\nEnter the port of reciever: ")) # it's 1300
IP4_client = input("\nEnter your IP address : ")  # 172.23.0.209
Port_client = int(input("\nEnter your port: "))  # 1400
username = input("username: ")  # Godspeed

print("Start Conversation....")

# Multi-threading
send = threading.Thread(target=client)
receive = threading.Thread(target=server)

send.start()
receive.start()


# To end the conversation we need to enter exit or end text from both the sides
## Thank You !!