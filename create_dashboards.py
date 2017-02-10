#!/usr/bin/env python
#-*- coding: UTF-8 -*-



##################################################################################
# version 1.0 release notes:
# Initial version
##################################################################################

import time
import datetime
import os
import sys

import json
from pymongo import MongoClient


########################################################################
# configuracion y variables globales


DB_MONGO_IP = "127.0.0.1"
DB_MONGO_PORT = 27017
DB_MONGO_NAME = "demos"


#### VARIABLES #########################################################

OUT_FOLDER = "/Users/Carlos/Workspace/Kyros/KyrosDashboard/dashboards"



########################################################################


########################################################################

########################################################################
# Definicion de clases
#
########################################################################

main():
    json '{"version":1,"allow_edit":true,"plugins":[],"panes":[{"title":"Coche Correos","width":1,"row":{"3":1},"col":{"3":3},"col_width":1,"widgets":[{"type":"gauge","settings":{"title":"Speed","value":"datasources[\"0904FMP\"][\"response\"][\"data\"][\"record\"][0][\"speed\"]","min_value":0,"max_value":100}},{"type":"pointer","settings":{"direction":"datasources[\"0904FMP\"][\"response\"][\"data\"][\"record\"][0][\"heading\"]","value_text":"datasources[\"0904FMP\"][\"response\"][\"data\"][\"record\"][0][\"heading\"]","units":"º"}}]},{"title":"Carlos Running","width":1,"row":{"3":1},"col":{"3":1},"col_width":2,"widgets":[{"type":"gauge","settings":{"title":"Velocidad","value":"datasources[\"Test_1\"][\"response\"][\"data\"][\"record\"][0][\"speed\"]","units":"Km/h","min_value":0,"max_value":"18"}},{"type":"sparkline","settings":{"title":"Altitud","value":["datasources[\"Test_1\"][\"response\"][\"data\"][\"record\"][0][\"altitude\"]"]}},{"type":"text_widget","settings":{"title":"Fecha","size":"regular","value":"datasources[\"Test_1\"][\"response\"][\"data\"][\"record\"][0][\"trackingDate\"]","animate":true}},{"type":"text_widget","settings":{"title":"Latitud","size":"regular","value":"datasources[\"Test_1\"][\"response\"][\"data\"][\"record\"][0][\"latitude\"]","sparkline":true,"animate":true}},{"type":"text_widget","settings":{"title":"Longitud","size":"regular","value":"datasources[\"Test_1\"][\"response\"][\"data\"][\"record\"][0][\"longitude\"]","sparkline":true,"animate":true,"units":"º"}},{"type":"google_map","settings":{"lat":"datasources[\"Test_1\"][\"response\"][\"data\"][\"record\"][0][\"latitude\"]","lon":"datasources[\"Test_1\"][\"response\"][\"data\"][\"record\"][0][\"longitude\"]"}}]},{"title":"Coche de Carlos","width":1,"row":{"3":17},"col":{"3":3},"col_width":1,"widgets":[{"type":"gauge","settings":{"title":"Velocidad","value":"datasources[\"1615-FDW\"][\"response\"][\"data\"][\"record\"][0][\"speed\"]","units":"Km/h","min_value":0,"max_value":"130"}}]}],"datasources":[{"name":"0904FMP","type":"JSON","settings":{"url":"https://api.kyroslbs.com/tracking1/vehicle/6","use_thingproxy":true,"refresh":2,"method":"POST","headers":[{"name":"x-access-token","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjIwOTA4MjY4NjU5MzMsImlzcyI6ImNydWVkYSIsInN1YiI6IlFjem1xaXFqc0JvMDIifQ.Vf1O_oIt-_pCqOP0yroA61ydJAMu2cZsMWdBHxu-GMk"}],"name":"0904FMP"}},{"name":"001Demo","type":"JSON","settings":{"url":"https://api.kyroslbs.com/tracking1/vehicle/667","use_thingproxy":true,"refresh":2,"method":"POST","headers":[{"name":"X-Access-Token","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjIwOTA4MjY4NjU5MzMsImlzcyI6ImNydWVkYSIsInN1YiI6IlFjem1xaXFqc0JvMDIifQ.Vf1O_oIt-_pCqOP0yroA61ydJAMu2cZsMWdBHxu-GMk"}]}},{"name":"Test_1","type":"JSON","settings":{"url":"https://api.kyroslbs.com/tracking1/vehicle/663","use_thingproxy":true,"refresh":1,"method":"POST","headers":[{"name":"x-access-token","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjIwOTA4MjY4NjU5MzMsImlzcyI6ImNydWVkYSIsInN1YiI6IlFjem1xaXFqc0JvMDIifQ.Vf1O_oIt-_pCqOP0yroA61ydJAMu2cZsMWdBHxu-GMk"}]}},{"name":"1615-FDW","type":"JSON","settings":{"url":"https://api.kyroslbs.com/tracking1/vehicle/13","use_thingproxy":true,"refresh":1,"method":"POST","headers":[{"name":"x-access-token","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjIwOTA4MjY4NjU5MzMsImlzcyI6ImNydWVkYSIsInN1YiI6IlFjem1xaXFqc0JvMDIifQ.Vf1O_oIt-_pCqOP0yroA61ydJAMu2cZsMWdBHxu-GMk"}]}}],"columns":3}'

    con = MongoClient(DB_MONGO_IP, int(DB_MONGO_PORT))
    db = con[DB_MONGO_NAME]
    user_collection = db['USER']

    print user_collection

if __name__ == '__main__':
    main()



