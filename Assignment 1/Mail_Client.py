import socket
import time
import base64



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = "smtp.cc.iitk.ac.in" 
port = 25     
sock.connect((address,port))

recv = sock.recv(1024)
recv = recv.decode()
print("Message after connection request:" + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
hiCommand = 'Hi \r\n'
sock.send(hiCommand.encode())
recv1 = sock.recv(1024)
recv1 = recv1.decode()
print("Message after Hi command:" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

#Info for username and password
username = "akshaym"
password = "*******"
 
base64_str = base64.b64encode(("\x00"+username+"\x00"+password).encode())
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
sock.send(authMsg)
recv_auth = sock.recv(1024)
print(recv_auth.decode())

mailFrom = "MAIL FROM:<akshaym@iitk.ac.in>\r\n"
sock.send(mailFrom.encode())
recv2 = sock.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)
rcptTo = "RCPT TO:<bibekp@iitk.ac.in>\r\n"
sock.send(rcptTo.encode())
recv3 = sock.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: "+recv3)
data = "DATA\r\n"
sock.send(data.encode())
recv4 = sock.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)
mail_subject = "Subject: testing client\r\n\r\n" 
sock.send(mail_subject.encode())
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + "\r\n\r\n"
sock.send(date.encode())

mail_body = input('Enter message:')
end = "\r\n.\r\n"
sock.send(mail_body.encode())
sock.send(end.encode())

recv_msg = sock.recv(1024)

print("Response after sending message body:"+recv_msg.decode())

quit = "QUIT\r\n"
sock.send(quit.encode())
recv5 = sock.recv(1024)
print(recv5.decode())
sock.close()