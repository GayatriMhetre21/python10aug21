#Find ASCII Value of a character 'X' and 'x'
c = 'x'
print("\nThe ASCII value of '" + c + "' is", ord(c))
c = 'X'
print("The ASCII value of '" + c + "' is", ord(c))




#Write Program to Compute Quotient and Remainder
n=9
s=4

q=n/s
print("\nQuotient is ",q)
r=n%s
print("Remainder is",r)




#Swap two numbers using temporary variable
x = 5
y = 10

temp = x        #created temporary variable 
x = y
y = temp        #created temporary variable 

print('\nThe value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))




#Write Program to Check Whether a Number is Even or Odd - 88,37,1658

num = int(input("\nEnter a number: "))
if (num % 2) == 0:
   print("\n{0} is Even".format(num))
else:
   print("\n{0} is Odd".format(num))



#Check whether an alphabet is vowel or consonant using if..else statement - a,b,e,o
ch = input("\nEnter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "\nis a Vowel")
else:
    print(ch, "\nis a Consonant")



#Write Programm to calculate GST i.e. 18% on base price 34900/-
gst = ((18/100) * 34900)
print("\nGST is ",)



#Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-
p=161258
t=1
r=5

print('The principal is', p)
print('The time period is', t)
print('The rate of interest is',r)
si = (p * t * r)/100
print('\nThe Simple Interest is', si)



#Write program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-

a=161258
e3=a/36
e5=a/60

emi3=e3+(0.05*e3)

emi5=e5+(0.05*e5)

print("\nEMI for 3 years with intrest 5%",emi3)

print("EMI for 5 years with intrest 5%",emi5)



      

