#2.program to rotate the list index values to next position and last one will become first position
def rotate_by_one(x):
    n=len(x)
    for i in range(0,n):
        temp=x[n-1]
        x[n-1]=x[i]
        x[i]=temp
    return x
l=[12,76,90,44,56,38]
print(l)
print(rotate_by_one(l))
    
