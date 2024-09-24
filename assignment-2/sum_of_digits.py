#6.Write a  Python program to calculate sum of digits of a number.
n=eval(input("Enter a number : "))
sum=0
while(n>=10):
    sum=sum+n%10
    n=n//10
sum=sum+n
print("sum of digits of given number :",sum)
