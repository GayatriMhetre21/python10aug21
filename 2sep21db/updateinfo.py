#- write a program update values in table
import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="update stdinform set address='akkalkote' where name='Gayatri' "
    cur.execute(query)
    print("execute query")
    mycon.commit()
    print(query+" values was updated successfully .... ")
except:
    print("values is not updated...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection close....")