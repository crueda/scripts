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

FILE = "./mail.log"
OUT = "./mail_stats.log"
OUT_DOMAIN = "./mail_domain_stats.log"

now = int(time.time())

########################################################################

# dictionary to store stats
mailStats = dict()
mailDomainStats = dict()

def readStats():
	global mailStats
	file = open(FILE, 'r')
	for line in file:
		vline = line.split(' to=<')
		if (len(vline)>1):
			for i in range (1,len(vline)):
				element = vline[i]
				if (element.find('@')>-1):
					mail = element[0:element.find('>')]
					domain = mail[mail.find('@')+1:len(mail)]
					#print domain
					#print mail
					if (mailStats.has_key(mail)):
						mailStats[mail] = mailStats[mail]+1
					else:
						mailStats[mail] = 1
					if (mailDomainStats.has_key(domain)):
						mailDomainStats[domain] = mailDomainStats[domain]+1
					else:
						mailDomainStats[domain] = 1

def writeStats():
	fid = open(OUT, 'w')
	nElements = len(mailStats.keys())
	i=1
	for key in mailStats.keys():
		if (i<nElements):
			fid.write("['" +  str(key) + "'," + str(mailStats[key]) + "],")
		else:
			fid.write("['" +  str(key) + "'," + str(mailStats[key]) + "]")
		i=i+1
	fid.close()

	fidDomain = open(OUT_DOMAIN, 'w')
	nElements = len(mailDomainStats.keys())
	i=1
	for key in mailDomainStats.keys():
		if (i<nElements):
			fidDomain.write("['" +  str(key) + "'," + str(mailDomainStats[key]) + "],")
		else:
			fidDomain.write("['" +  str(key) + "'," + str(mailDomainStats[key]) + "]")
		i=i+1
	fidDomain.close()


readStats()
writeStats()

print mailStats


sys.exit(0)


