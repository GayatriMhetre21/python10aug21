#Find ASCII Value of a character 'X' and 'x'
c = 'x'
print("The ASCII value of '" + c + "' is", ord(c))

#Write Program to Compute Quotient and Remainder
n=9
s=4

q=n/s
print("Quotient is ",q)
r=n%s
print("Remainder is",r)

#Swap two numbers using temporary variable
x = 5
y = 10

temp = x        #created temporary variable 
x = y
y = temp        #created temporary variable 

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


#Write Program to Check Whether a Number is Even or Odd - 88,37,1658

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


#Check whether an alphabet is vowel or consonant using if..else statement - a,b,e,o
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")









#Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-

    p=161258
    t=30
    r=5
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si)
    

      

