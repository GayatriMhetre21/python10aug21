#list
x=[2,3,4,5,6,7,8,9,1,0]#declare list type which carry 10 element

#extract all list
print("list x=",x[0:1])
print("list x=",x[0:5])
print("list x=",x)
print("list x=",x[7])
print("list x=",x[0:9])
print("list x=",x[1:9])
print("list x=",x[0:10])
print("list x=",x[10:0])

#extract index number 2 to 5
print("\nlist x=",x[2:5])

#print list element reverse
print("\nList x in reverse:",x[::-1])

#using append,insert add element in list
x.append(11)
print("\nAfter add 11 value in list = ",x)

x.insert(3,"hi")
print("\ninsert hi in list",x)

#Using pop,remoe,del remove element
x.pop(8)
print("\nlist After pop x[8]=",x)

x.remove(4)
print("\nlist After remove x[4]=",x)

del(x[9])
print("\nlist After delete x[9]",x)

x.clear()
print("\nlist After clear list ",x)

#tuple
g=[2,3,4,5,6,7,8,9,1,0]
#declare tuple type which carry 10 element

#extract all tuple
print("\ntuple g=",g)

#extract index number 2 to 5
print("\ntuple g=",g[2:5])

#print tuple element reverse
print("\ntuple g in reverse:",g[::-1])


#use index and count function
z=g.index(1)
print("\nIndex of 1=",z)

z=g.count('4')
print("\nCount of 4 is =",z)