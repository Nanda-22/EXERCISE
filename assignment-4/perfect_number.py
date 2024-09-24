#7.Write a Python function to check whether a number is "Perfect" or not.
n=eval(input("Enter a number : "))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print("the factors of given number",n,"is",l)
sum=0
for i in range(0,len(l)):
    sum=sum+l[i]
if sum==2*n:
    print("The given number",n,"is a perfect number")
else:
    print("The given number",n,"is not a perfect number")
