# write a program to demostration control flow statement.

#if
a=40
n=int(input("\nEnter a number= "))
if a<n:
    print(a, "less than",n)


#ifelse
q=30
if q>n:
    print(q,"\nis greater than",n)
else:
    print(q,"\nis smaller than",n)



#elif
g=int(input("\nEnter a number= "))
if g>0 :
    print(g,"\nis positive number")
elif g==0:
        print("\nNumber is zero")
else:
    print(g,"\nis negative number")



# forloop
list=[2,4,6,8,10]
sum=0
for num in list:
    sum=sum+num
    print("sum ",sum)



# whileloop
i = 1
while i < 8:
  print(i)
  i += 1


# Pass
if 10>5:
    pass



# break
for o  in "python":
    if o=='i':
        break
    print(o)



# continue
for o  in "programs":
    if o=='i':
        continue
    print(o)