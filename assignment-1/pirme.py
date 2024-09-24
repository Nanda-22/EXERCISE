#4.Write a program to check whether a given number is prime or not
n=int(input("Enter a number : "))
for i in range(2,n):
    if(n%i==0):
        print("Given number",n,"is not a prime number")
        break
    else:
        print("Given number",n,"is a prime number")
        break
