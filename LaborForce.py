import numpy as np
try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb
import sys

try:
    db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="password", db="mydatabase")
    cursor = db.cursor()
except:
    print('Database is not combind')
    sys.exit()
selectData=''
if len(sys.argv)>1:
    selectData=sys.argv[1]

sqlcmd = "SELECT `Year`,`SEX`,`" + selectData + "` FROM `LaborForce`ORDER BY `Year`"

try:
    cursor.execute(sqlcmd)
    result = cursor.fetchall()
    for row in result:
        print(row,'<br>')

except:
    print('error,please check.')

#育銓好大我是說拳頭



