#-write a program to create table stdinfo
import MySQLdb

try:
    query="create table stdinform(name varchar(50),rollno varchar(10),address varchar(50))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    cur.execute(query)
    print("excecute excecute")
    print("execute query")
    mycon.commit()
    print(query+"table created successfully.... ")
except:
    print("table is not created...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection close....")