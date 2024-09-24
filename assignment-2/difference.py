#1.Write a Python program to calculate the difference between a given number and 23. If the number is greater than 23, return twice the absolute difference.
n=int(input("Enter a number : "))
def diff(num):
    if(num<=23):
        print("The difference between given number and 23 is : ",(23-num))
    else:
        print("The difference between given number and 23 is : ",(num-23))
        return ((num-23)*2)
print(diff(n))
