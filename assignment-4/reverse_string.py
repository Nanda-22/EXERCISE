#5.Write a Python program to reverse a string.
s="nanda"
print(s[::-1])
#by using function reverse string
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
