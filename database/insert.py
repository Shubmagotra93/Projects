import mysql.connector as myconn

mydb = myconn.connect(host="localhost", user= "root", password = "Rootuser@123", database= "LearnCoding")
db_cursor = mydb.cursor()

db_cursor.execute("insert into Emp(Roll, Ename) values(%s, %s)" ,(10, "Ankush"))
mydb.commit()