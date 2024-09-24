#3.program to get nth even number by reading n value
def even_number(n):
    count=0
    for i in range(0,2*n):
        if(i%2==0):
            count+=1
        if(count==n):
            return i
N=eval(input("Enter a number : "))
print(even_number(N))
