#5.Write a program to print the following pattern of right angled triangle
n=eval(input("Enter a number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(end="\n")
