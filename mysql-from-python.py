import os
import datetime
import pymysql

username = os.getenv('GITPOD_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    with connection.cursor() as cursor:
        cursor.execute("""create table if not exists
                        Friends(name char(20), age int, DOB datetime);""")
finally:
    connection.close()