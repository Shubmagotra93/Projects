import mysql.connector as myconn

mydb = myconn.connect(host="localhost", user= "root", password = "Rootuser@123")
db_cursor = mydb.cursor()
db_cursor.execute("create database LearnCoding")
