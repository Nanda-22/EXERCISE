#10.Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
l=[2,4,6,8,25,45,68,97,39]
print("list elements before swap : ",end="")
for i in range(0,len(l)):
    print(l[i],end=" ")
print("\nEnter swapping positions must be less than length of list, length of list : ",len(l))
j=int(input("Enter a first place term to swap : "))
k=int(input("Enter a second place term to swap : "))
if(j and k<=len(l)):
    temp=l[j]
    l[j]=l[k]
    l[k]=temp
else:
    print("Enter a correct swapping position") 
print("list elements after swap : ",end="")
for i in range(0,len(l)):
    print(l[i],end=" ")
