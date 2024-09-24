#1.operators
def operate(x,y,o):
    if(o=="+"):
        return x+y
    elif(o=="-"):
        return x-y
    elif(o=="*"):
        return x*y
    elif(o=="/"):
        return x/y
    elif(o=="%"):
        return x%y
    elif(o=="//"):
        return x//y

X=eval(input("Enter x : "))
Y=eval(input("Enter y : "))
O=eval(input("Enter operator : "))
print(operate(X,Y,O))
