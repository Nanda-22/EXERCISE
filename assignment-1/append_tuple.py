#15.Create a tuple with all even numbers from 1 to 20 using a for loop
t=()
l=[]
print(type(t))
for i in range(1,20+1):
    r=i%2
    if(r==0):
        l.append(l[i])
print("The even numbers in range of 1 to 20 : ",end="")
for i in range(0,20):
    print(t(i),end=" ")
