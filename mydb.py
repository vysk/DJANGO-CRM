# Install MySQL on your computer
# https://dev.mysql.com/dowloads/installer
# pip install mysql
# pip install mysql-connetcor
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

#prepare a curser object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE dcrm")

print("Database created!")