#2.Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
x=int(input("Enter a number : "))
y=int(input("Enter a number : "))
if(x==y):
    print("The GCD of",x,"and",y,"is : ",x)
elif(x>y):
    for i in range(1,y+1):    
        r=x%y
        if(r==0):
            print("The GCD of",x,"and",y,"is : ",y)
            break
        else:
            x=y
            y=r        
elif(x<y):
    for i in range(1,x+1):
        r=y%x
        if(y%x==0):
            print("The GCD of",x,"and",y,"is : ",x)
            break
        else:
            y=x
            x=r
