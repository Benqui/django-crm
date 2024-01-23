import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'plicky01'
)

#prepare cursor object 

cursorObject = dataBase.cursor()


#create the db

cursorObject.execute("CREATE DATABASE  crmdb")

print("Ya quedo we \n")