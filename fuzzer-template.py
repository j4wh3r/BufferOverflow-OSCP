#!/usr/bin/env python2

import sys, socket
from time import sleep


ip = ""
port = 
prefix = " "
postfix= ""
buff = "A" * 100

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port ))
		print "sending %s bytes"%str(len(buff))
		
		s.send(prefix + buff + postfix)
		sleep(1)
		buff += "A" * 100
	except:
		print "fuzzing crasched at %s bytes" %str(len(buff))
		sys.exit()
