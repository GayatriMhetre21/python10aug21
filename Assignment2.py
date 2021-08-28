print("\n\t\t ***   ASSIGNMENT 2   ***\n")

#2)Write a program to generate employee ID-Card(image not required,id card show on console)
print(" -->  * Answer of 2nd question *")
class Employee:
    __id=0
    __name=""
    __gender=""
    __city=""
    __salary=0
    def setData(self):
        self.__id=int(input("Enter Id\t:\t"))
        self.__name = input("Enter Name\t:\t")
        self.__gender = input("Enter Gender\t:\t")
        self.__city = input("Enter City\t:\t")
        self.__salary = int(input("Enter Salary\t:\t"))
    def showData(self):
        print("\t\tId\t\t:\t\t",self.__id)
        print("\t\tName\t\t:\t\t", self.__name)
        print("\t\tGender\t\t:\t\t", self.__gender)
        print("\t\tCity\t\t:\t\t", self.__city)
        print("\t\tSalary\t\t:\t\t", self.__salary)

def main():
    print("\n\t\t $$  Enter Employee Info For Id Card   $$ \t\n")
    #Employee Object
    emp=Employee()
    emp.setData()
    print("\n\t\t****      Employee Id Card      ****  \n")
    emp.showData()

if __name__=="__main__":
    main()


#3)Write programm to read file and make Arithematic operation using file content.(File attached : "math.txt")
print("\n --> * Answer of 3rd question *\n")
with open("math.txt",'r',encoding='utf-8') as f:
     print(f.read())
     f.close()