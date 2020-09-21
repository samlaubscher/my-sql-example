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
        rows = [("Bob", 21, "1990-02-06 23:12:03"),
                ("Jim", 56, "1993-03-09 21:11:13"),
                ("Tim", 31, "1970-02-06 23:12:03"),
                ("Matt", 51, "1980-02-06 23:12:03")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    connection.close()