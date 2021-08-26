#using with to write
with open ("text.txt",'w',encoding='utf-8') as f:
    f.write("Using with to write into file")
    f.close()

#using with to read from file
with open("text.txt",'r',encoding='utf-8') as f:
     print(f.read())
     f.close()

#write using binary 
f=open("text.txt",'wb')
f.write(b"Using binary to write")
f.close()

#write file using object
try:
    f=open("text.txt",'w',encoding="utf-8")
    f.write("Using Object method ")
except:
    print("Not available")
finally:
     f=open("text.txt",'w',encoding="utf-8")
     f.close()

#using binary read
f=open("text.txt",'rb')
print(f.read())
f.close()

#read file using object
try:
    f=open("text.txt",'r',encoding='utf-8')
    print(f.read())
except:
     print("Not available")
finally:
    f=open("text.txt",'r',encoding="utf-8")
    f.close()