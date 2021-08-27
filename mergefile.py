import shutil
print("Enter 'x' for exit...")
filename1=input("Enter First file name ;")
if Filename1=='x':
    exit()
else:
        filename2=input("enter second file name ;")
        filename3=input("create new file to merge content ....;")
        with open(filename3,'wb') as wfd:
            for f in [filename1,filename2]:
                with open(f,'rb') as fd:
                    shutil.copyfileobj(fd,wfd,1024*1021*10)
print("\n content merged successfully... do you want to see : press")
check = input()
if check=='n':
        exit()
else:
        c=open(filename3,'r')
        print(c.read())
        c.close()
