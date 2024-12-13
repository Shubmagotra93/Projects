import mysql.connector as myconn

mydb = myconn.connect(host="localhost", user= "root", password = "Rootuser@123", database= "LearnCoding")
db_cursor = mydb.cursor()
# db_cursor.execute("create table Emp2(Roll int, Ename varchar(20))")
db_cursor.execute("show tables")
# print(db_cursor)
for table in db_cursor:
    print(table)
