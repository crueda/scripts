#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import MySQLdb
import psycopg2
import time

# MySQL
#DB_IP = "192.168.28.251"
DB_IP = "172.26.5.7"
DB_PORT = 3306
DB_NAME = "kyros4"
DB_USER = "root"
DB_PASSWORD = "dat1234"

INIT_DATE=1493589600000
END_DATE=1496268000000

conn_string = "host='192.168.28.181' dbname='cartodb_dev_user_da4a0138-8e15-4485-b920-9ece3a11fae7_db' user='postgres' password='dat1234'"
#conn_string = "host='127.0.0.1' dbname='cartodb_dev_user_da4a0138-8e15-4485-b920-9ece3a11fae7_db' user='postgres' password='dat1234'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

def executeMySQLSelect(QUERY):
    try:
        dbConnection = MySQLdb.connect(DB_IP, DB_USER, DB_PASSWORD, DB_NAME)
        try:
            cursor = dbConnection.cursor()
            cursor.execute("SET NAMES \'utf8\'")
            cursor.execute(QUERY)
            rows = cursor.fetchall()
            cursor.close()
            dbConnection.close()
            return rows
        except Exception, error:
            print 'Error executing query %s: %s' % (QUERY, error)
    except Exception, error:
		print 'Error connecting to database: %s' % str(error)


def getTracking(initDate, endDate):
    try:
        query = "select VEHICLE_LICENSE as vehicle_license, DEVICE_ID as deviceId, (POS_LATITUDE_MIN/60)+POS_LATITUDE_DEGREE as latitude, (POS_LONGITUDE_MIN/60)+POS_LONGITUDE_DEGREE as longitude, GPS_SPEED as speed, ALTITUDE as altitude, HEADING as heading, DISTANCE as distance, BATTERY as battery, TRACKING_ID as tracking_id, POS_DATE as posDate from TRACKING where POS_DATE>" + str(initDate) + " and POS_DATE<" + str(endDate)
        print query
        result = executeMySQLSelect(query)
        return result
    except Exception, error:
        print 'Error at function getTracking: %s' % (str(error))

tracking = getTracking(INIT_DATE, END_DATE)
for entry in tracking:
    geom = "ST_GeomFromText('POINT(" + str(entry[3]) + " " + str(entry[2]) + ")', 4326)"
    posdate = entry[10]/1000
    isoDate = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(posdate))
    query =  "INSERT INTO tracking_hawkeye (vehicle_license, device_id, latitude, longitude, speed, altitude, heading, distance, battery, the_geom, tracking_id, date) VALUES ('" + str(entry[0]) + "'," + str(entry[1]) + "," + str(entry[2]) + "," + str(entry[3]) + "," + str(entry[4]) + "," + str(entry[5]) + "," + str(entry[6]) + "," + str(entry[7]) + "," + str(entry[8]) + "," + geom + "," + str(entry[9]) + ",'" + isoDate + "')"
    print query
    cursor.execute(query)
    conn.commit()
