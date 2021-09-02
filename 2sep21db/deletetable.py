#-write a program to delete table

import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="drop table stdinform"
    cur.execute(query)
    print("excecute excecute")
    print("execute query")
    mycon.commit()
    print(query+"table deleted successfully .... ")
except:
    print("table not deleted ")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection close....")