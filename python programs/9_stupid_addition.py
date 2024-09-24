#9.program for addition of integers and strings of same data type and if not return none
def stupid_addition(x,y):
    if(type(x)==type(y)):
        return x+y
    else:
        return None
X=eval(input("Enter a value : "))
Y=eval(input("enter a value : "))
print("The result of given values to the function : ",stupid_addition(X,Y))
