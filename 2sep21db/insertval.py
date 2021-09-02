# -write a program to insert values in table
import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="insert into stdinform values('Gayatri','2533','solapur')"
    cur.execute(query)
    print("excecute excecute")
    print("execute query")
    mycon  .commit()
    print(query+"values inserted successfully .... ")
except:
    print("values is not inserted...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection close....")