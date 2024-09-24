#13.program to change every letter in given string into next letter in alphabet
def move(s):
    for i in range(0,len(s)):
        print(chr(ord(s[i])+1),end="")
S=eval(input("Enter a string : "))
print("The string before change : ",S)
print("The string after changed to next letter of every character of given string : ",end="")
move(S)
