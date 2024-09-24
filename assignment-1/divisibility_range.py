#1.Write a program which will find all such numbers which are divisible by 5 but are not a multiple of 11, between 1000 and 2000 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
print("The values are : ",end="")
for i in range(1000,2000+1):
    if(i%5==0):
        if(i%11!=0):
            print(i,end=",")
