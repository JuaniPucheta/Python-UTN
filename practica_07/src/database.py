import mysql.connector

database = mysql.connector.connect(
    host="localhost",           # your host, usually localhost (could be an IP address)
    user="root",                # your username
    password="root",            # your password
    database="python-flask"     # name of the data base
)