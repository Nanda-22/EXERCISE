#6.program to create a calculator using class and methods
class calculator():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(x,y):
        return x+y
    def substraction(x,y):
        return x-y
    def multiplication(x,y):
        return x*y
    def division(x,y):
        return x/y
X=eval(input("Enter first number : "))
Y=eval(input("Enter second number : "))
print("The addition of given numbers  : ",calculator.add(X,Y))
print("The substraction of given numbers  : ",calculator.substraction(X,Y))
print("The multiplication of given numbers  : ",calculator.multiplication(X,Y))
print("The division of given numbers  : ",calculator.division(X,Y))
