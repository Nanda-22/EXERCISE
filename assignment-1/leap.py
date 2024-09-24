#8.Write a program to check whether a year is a leap year or not?
n=int(input("Enter a year : "))
if(n%4!=0 or n%100!=0 or n%400!=0):
    print("The given year",n,"is not a leap year")
else:
    print("The given year",n,"is a leap year")
