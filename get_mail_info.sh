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
import subprocess
from datetime import date, timedelta
import requests
import json


#### VARIABLES #########################################################

RELEVANT_STATS = ["TOTAL", "API_LOGIN", "APP_LOGIN", "APP_NOTIFICATIONS"]

FILE = "/tmp/stats_api"

now = int(time.time())

########################################################################

# dictionary to store stats
nowStats = {}

def getSTATS():
	r = requests.get("http://192.168.28.251:3003/stats")
	stats_json = json.loads(r.content)
	total_requests = stats_json['counter']
	api_login = stats_json['requests']["/login"]
	app_login = stats_json['requests']["/api/app/login"]
	app_notifications = stats_json['requests']["/api/app/notificationLimit"]
	return [['TOTAL',total_requests],['API_LOGIN',api_login],['APP_LOGIN',app_login],['APP_NOTIFICATIONS',app_notifications]]

def writeStats(stats):
	try:
		os.remove(FILE)
	except:
		pass
	fid = open(FILE, 'w')
	fid.write("timestamp:" +  str(now) + "\n")
	for values in RELEVANT_STATS:
		fid.write(values + ":" + stats[values] + "\n")
	fid.close()
	sys.exit(0)

stats = getSTATS()
nowStats = {
	"TOTAL": str(stats[0][1]),
	"API_LOGIN": str(stats[1][1]),
	"APP_LOGIN": str(stats[2][1]),
	"APP_NOTIFICATIONS": str(stats[3][1])
}
def readStats():
	try:
		with open(FILE, "r") as ins:
			old_stats = {}
			for line in ins:
				data = line.split(":")
				old_stats[data[0]]=data[1][0:len(data[1])-1]
		return old_stats
	except:
		writeStats(nowStats)
	sys.exit(0)


#writeStats(nowStats)

# fisrt we read las stats
lastStats = readStats()

secondsFromLast = now - int( lastStats["timestamp"])
minutesFromLast = (now - int( lastStats["timestamp"]) )/60
totalFromLast = int(nowStats["TOTAL"]) - int(lastStats["TOTAL"])
apiLoginFromLast = int(nowStats["API_LOGIN"]) - int(lastStats["API_LOGIN"])
appLoginFromLast = int(nowStats["APP_LOGIN"]) - int(lastStats["APP_LOGIN"])
appNotificationsFromLast = int(nowStats["APP_NOTIFICATIONS"]) - int(lastStats["APP_NOTIFICATIONS"])

if (minutesFromLast==0):
	totalAv = 0
	apiLoginAv = 0
	appLoginAv = 0
	appNotificationsAv = 0
else:
	totalAv = int(totalFromLast/minutesFromLast)
	apiLoginAv = int(apiLoginFromLast/minutesFromLast)
	appLoginAv = int(appLoginFromLast/minutesFromLast)
	appNotificationsAv = int(appNotificationsFromLast/minutesFromLast)

print "OK - Kyros API stats| %s=%s %s=%s %s=%s %s=%s" % ("TOTAL_REQUESTS", totalAv, "API_LOGIN", apiLoginAv, "APP_LOGIN", appLoginAv, "APP_NOTIFICATIONS", appNotificationsAv)

writeStats(nowStats)
sys.exit(0)


