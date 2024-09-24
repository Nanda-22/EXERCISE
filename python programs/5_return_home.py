#5.program to give exact directions to get back to home position
def back_to_home(x):
    if(x==path[::-1]):
        return True
    else:
        return False

path="NESW"
print("The path is : ",path)
return_path=eval(input("Enter the return path : "))
print("The path to get back to home : ",return_path)
print(back_to_home(return_path))
