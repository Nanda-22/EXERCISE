#4.Write a Python function that prints out the first n rows of Pascal's triangle.
n=eval(input("Enter a number : "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()
