#!/usr/bin/env python
# -*- coding: utf-8 -*-

# autor: Carlos Rueda Morales
# date: 2017-03-03
# mail: carlos.rueda@deimos-space.com
# version: 1.0

###################################################################################################
# version 1.0 release notes:
# Initial version
####################################################################################################

import string, cgi, time
import time
import sys
import datetime
import os
import logging, logging.handlers
from datetime import date, timedelta


#### VARIABLES #########################################################

RELEVANT_STATS = ["TOTAL", "API_LOGIN", "APP_LOGIN", "APP_NOTIFICATIONS"]

FILE = "./mail.log"
OUT = "./mail_stats.csv"

now = int(time.time())

########################################################################

# dictionary to store stats
nowStats = {}

def readStats():
	file = open(FILE, 'r')
	for line in file:
		vline = line.split(' to=<')
		if (len(vline)>1):
			for i in range (1,len(vline)):
				element = vline[i]
				if (element.find('@')>-1):
					print element[0:element.find('>')]

def writeStats(stats):
	fid = open(OUT, 'w')
	fid.write("timestamp:" +  str(now) + "\n")
	#for values in RELEVANT_STATS:
	#	fid.write(values + ":" + stats[values] + "\n")
	fid.close()



nowStats = readStats()

print "OK"

sys.exit(0)


