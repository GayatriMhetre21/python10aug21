 
 # 1) Reverse a String and print it on console"Python Skills" .

print("\n*Answer of 1st question*")
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]  
s = "Python Skills"  
print ("\nThe original string  is = ",end="")
print (s)
print ("The reversed string is = ",end="")
print (reverse(s))


# 2) Assign String to x variable in DD-MM-YYYY format
  # extract and print Year from String.

print("\n*Answer of 2nd question*")
print()
import datetime
date_str = '29/12/2017' 
format_str = '%d/%m/%Y'
year='two thousand and seventeen'
datetime_obj = datetime.datetime.strptime(date_str, format_str)
print(datetime_obj.date())
print ("\nYear in String =",year)


# 3) In a small company, the average salary of three employees is Rs1000 per week.
#  If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn?
#  Solve by using python programm.

print("\n*Answer of 3rd question*")
average = 1000
e1 = 1100
e2 = 500
e3 = (average - (e1 + e2)/3)*3                  
print("\nSalary of Third employee is= ", e3)



#4) Write Program - convert a percentage to a fraction (To convert a percentage into fraction let say 30%
#to a fraction)
print("\n*Answer of 4th question*")
per = 30
fraction = per / 100
print ("\nFraction of 30% is =",fraction)



#5)Write Program - A train 340 m long is running at a speed of 45 km/hr. 
#what time will it take to cross a 160 m long tunnel   

print("\n*Answer of 5th question*")
trainlength = 340
tunnellength = 160
total = trainlength + tunnellength
speed = 45
mps = 5/18
time = total / (45 * mps)
print ("\nTotal time of train to cross the tunnel is = ",time)
