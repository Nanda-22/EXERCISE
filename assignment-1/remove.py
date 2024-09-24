#13.Write a program to delete an item from the list.
l=[2,4,6,8,25,45,68,97,39]
n=int(input("Enter a how many elements to remove in list : "))
print("ELements before removing : ",end="")
for j in range(0,len(l)):
    print(l[j],end=" ")
print(end="\n")
for i in range(1,n+1):
    x=int(input("Enter a which position is to remove : "))
    l.remove(l[x])
print("ELements after removing : ",end="")
for i in range(0,len(l)):
    print(l[i],end=" ")
