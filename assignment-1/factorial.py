#2.Write a program to find the factorial of a number
n=int(input("Enter a number : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("The factorial of a given number",n,"is : ",fact)
