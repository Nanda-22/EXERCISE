#4.program to find total number of legs of given different types of animals
def animals(x,y,z):
    chicken_legs=2*x
    cows_legs=4*y
    pigs_legs=4*z
    total_legs=chicken_legs+cows_legs+pigs_legs
    return total_legs
chicken=eval(input("Enter number of chickens : "))
cows=eval(input("Enter number of cows : "))
pigs=eval(input("Enter number of pigs : "))
print("Total number of legs for given animals are : ",animals(chicken,cows,pigs))
