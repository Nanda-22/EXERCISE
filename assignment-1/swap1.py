#9.Given a list, write a Python program to swap first and last element of the list
l=[2,4,6,8,25,45,68,97,39]
print("list elements before swap : ",end="")
for i in range(0,len(l)):
    print(l[i],end=" ")
temp=l[0]
l[0]=l[(len(l)-1)]
l[(len(l)-1)]=temp
print("\nlist elements after swap : ",end="")
for i in range(0,len(l)):
    print(l[i],end=" ")
