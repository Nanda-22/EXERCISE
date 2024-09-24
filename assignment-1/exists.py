#11.Write a program to check whether an element exists in the list using Python
l=[2,4,6,8,25,45,68,97,39]
n=int(input("Enter a number : "))
for i in range(0,len(l)):
    if(n==l[i]):
        print("The given number",n,"is available in list")
        break
    
