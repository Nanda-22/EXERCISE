#14.Write a program to remove all odd numbers from the list.
l=[2,4,6,8,25,45,68,97,39]
print("Elements before removing odd numbers : ",end="")
for i in range(0,len(l)):
    print(l[i],end=" ")
print(end="\n")
print(len(l))
for i in range(0,len(l)):
    if(l[i]%2==1):
        l.remove(i)
print("Elements after removing odd numbers : ",end="")
for i in range(0,len(l)):
    print(l[i],end=" ")
