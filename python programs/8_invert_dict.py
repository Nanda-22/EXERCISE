#8. program to invert the values and keys in dictionary
def invert(x):
    for key, value in dict.items():
        r_dict[value] = key
    return r_dict
dict={1:2,'a':'b',"apple":"banana"}
r_dict={}
print("The dictionary before invertion : ",dict)
print("The dictionary after invertion : ",invert(dict))

