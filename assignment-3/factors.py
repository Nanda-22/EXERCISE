#2. Write a Python program to find the factors of a given number and append it to a list.
# And also For each of the factor in the list find the multiples of the factor in the list and print them.
n=int(input("Enter a number : "))
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
print("The factors of given number are : ",end="")
for j in range(0,len(l)):
    print(l[j],end=" ")
print("\n")
for j in range(1,n+1):
    for k in range(0,len(l)):
        if(n==(j*l[k])):
            print("The multiple for",j,"is",l[k])

