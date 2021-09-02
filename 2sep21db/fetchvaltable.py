#-write a program fetch values from table
import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="select * from stdinform"
    cur.execute(query)
    print("execute query")
    tdata=cur.fetchall()
    print("values are ")

    for row in tdata:

        print("name : ",row[0])
        print("rollno : ",row[1])
        print("address : ",row[2])
except:
    print("table is no fatched...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection close....")