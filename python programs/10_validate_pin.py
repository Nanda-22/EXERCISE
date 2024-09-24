#10.program that the given pin is validate or not
def validate_pin(x):
    if(len(x)==4 or len(x)==6):
        if(x.isnumeric()==True):
            return True
        else:
            return False
X=eval(input("Enter a pin : "))
print(validate_pin(X))
