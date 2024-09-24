#3.Write a Python function to check whether a string is a pangram or not.
def ispangram(str):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        if char not in str.lower():
            return False

    return True

string="the quick brown fox jumps over the lazy dog"
if(ispangram(string)==True):
    print("The given string is pangram")
else:
    print("The given string is not a pangram")
