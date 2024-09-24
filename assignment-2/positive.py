#8.Write a Python program to filter positive numbers from a list.
l=[2,6,-87,56,-9,5,-65,-98,80]
for i in range(0,len(l)):
    if(l[i]<0):
        l.remove(l[i])
for i in range(0,len(l)):
    print(l[i],end=" ")
