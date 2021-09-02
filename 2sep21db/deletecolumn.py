#-write program to delete specific row of table

import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="alter table stdinform drop column moblie"
    cur.execute(query)
    print("excecute excecute")
    print("execute query")
    mycon.commit()
    print(query+"column deleted successfully .... ")
except:
    print("column not deleted ")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection close....")