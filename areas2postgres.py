#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import MySQLdb
import psycopg2
import time

# MySQL
#DB_IP = "192.168.28.251"
DB_IP = "172.26.6.7"
DB_PORT = 3306
DB_NAME = "kyros4"
DB_USER = "root"
DB_PASSWORD = "dat1234"


conn_string = "host='192.168.28.181' dbname='cartodb_dev_user_da4a0138-8e15-4485-b920-9ece3a11fae7_db' user='postgres' password='dat1234'"
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


def getAreas():
    try:
        query = "select AREA.ID, AREA.DESCRIPTION, AREA.TYPE_AREA from AREA where AREA.RADIUS is null and DESCRIPTION not LIKE 'DELETE_%'"
        print query
        result = executeMySQLSelect(query)
        return result
    except Exception, error:
        print 'Error at function getAreas: %s' % (str(error))

def getAreasCircular():
    try:
        query = "select AREA.ID, AREA.DESCRIPTION, AREA.TYPE_AREA, AREA.RADIUS from AREA where AREA.RADIUS is not null and DESCRIPTION not LIKE 'DELETE_%' and DATE_END>1495464289000"
        print query
        result = executeMySQLSelect(query)
        return result
    except Exception, error:
        print 'Error at function getAreas: %s' % (str(error))

def getGeom(areaId):
    try:
        query = "select (POS_LATITUDE_MIN/60)+POS_LATITUDE_DEGREE as latitude, (POS_LONGITUDE_MIN/60)+POS_LONGITUDE_DEGREE as longitude from VERTEX where AREA_ID=" + str(areaId) + " order by NUM_VERTEX"
        #print query
        result = executeMySQLSelect(query)
        geom = "ST_GeomFromText('POLYGON(("
        num_element = 0
        for entry in result:
            if (num_element == 0):
                geom = geom + str(entry[1]) + " " + str(entry[0])
            else:
                geom = geom + "," + str(entry[1]) + " " + str(entry[0])
            num_element += 1

        if ( (result[0][0] != result[len(result)-1][0]) or (result[0][1] != result[len(result)-1][1]) ):
            geom = geom + "," + str(result[0][1]) + " " + str(result[0][0])

        geom = geom + "))', 4326)"
        return geom
    except Exception, error:
        print 'Error at function getGeom for area ' + str(areaId) + ': %s' % (str(error))

def getGeomCircular(areaId, radius):
    try:
        query = "select (POS_LATITUDE_MIN/60)+POS_LATITUDE_DEGREE as latitude, (POS_LONGITUDE_MIN/60)+POS_LONGITUDE_DEGREE as longitude from VERTEX where AREA_ID=" + str(areaId)
        #print query
        result = executeMySQLSelect(query)
        geom = "ST_BUFFER(ST_GeomFromText('POINT("
        entry = result[0]
        geom = geom + str(entry[1]) + " " + str(entry[0])
        radio = float(radius)/float(100000)
        geom = geom + ")', 4326)," + str(radio) + ",'quad_segs=8')"
        #geom = geom + ")', 4326)," + "0.02" + ",'quad_segs=50')"
        return geom
    except Exception, error:
        print 'Error at function getGeomCircular for area ' + str(areaId) + ': %s' % (str(error))




areas = getAreas()
for entry in areas:
    geom = getGeom(entry[0])
    if (geom!=None):
        query =  "INSERT INTO area_kyros (name, area_type, the_geom) VALUES ('" + str(entry[1]) + "','" + str(entry[2]) + "'," + str(geom) + ")"
        #print query
        try:
            cursor.execute(query)
            conn.commit()
        except Exception, error:
            print 'Error para la zona' + str(entry[0]) + ': %s' % (str(error))


areasCircular = getAreasCircular()
for entry in areasCircular:
    geom = getGeomCircular(entry[0], entry[3])
    if (geom!=None):
        query =  "INSERT INTO area_kyros (name, area_type, the_geom) VALUES ('" + str(entry[1]) + "','" + str(entry[2]) + "'," + str(geom) + ")"
        #print query
        try:
            cursor.execute(query)
            conn.commit()
        except Exception, error:
            print 'Error para la zona' + str(entry[0]) + ': %s' % (str(error))
