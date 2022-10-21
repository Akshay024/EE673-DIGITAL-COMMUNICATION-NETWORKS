# Program for UDP client
#import modules 

import socket
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #   Create UDP scoket for server
address = '172.23.0.209'        # IP address of system 
port = 12000
sock.settimeout(1)

total_rtt = 0
lost_packet = 0 
maximum_RTT = 0
minimum_RTT = 999999

for i in range(10):
    
    sock.sendto("ping".encode(),(address,port))
    start_time = time.monotonic_ns()
    print("Pinged")

    try:
        pong, _ = sock.recvfrom(1024)
        receive_time = time.monotonic_ns()
        delay = (receive_time-start_time)/1000
    
        print(pong.decode(),"RTT =", delay, "ms")
        
        total_rtt += delay
        maximum_RTT = max(maximum_RTT, delay)
        minimum_RTT = min(minimum_RTT, delay)
    
    except socket.timeout:
        lost_packet += 1        
        print("PING %i Request timed out\n" % (i+1))

print(total_rtt)
print(maximum_RTT)
print(minimum_RTT)
print(lost_packet)