#1.Write a Python program to print the Fibonacci sequence. If a number is given, find whether it belongs to the Fibonacci sequence and if so which term is the number?
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
r=int(input("Enter a range : "))
l=[]
for i in range(r):
    print(fib(i),"end=" "")
    l.append(fib(i))
num=int(input("Enter a number : "))
for j in range(0,len(l)):
    if(l[j]==num):
        print(f"The given number ",l[i]," is in fabinacci series and it is ",i,"th term in list l")
    else:
        print("Enter a correct number")
