#- write program to alter table

import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="alter table stdinform add moblie int(10)"
    cur.execute(query)
    print("excecute excecute")
    print("execute query")
    mycon.commit()
    print(query+"values altered successfully .... ")
except:
    print("values is not altered...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection close....")