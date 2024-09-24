#6.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
l=[15,678,123,76,980,441,56,84,286]
print("The values before l1 is created for below 100 values : ",l)
l1=[]
for i in range(0,len(l)):
    if l[i]<100:
        l1.append(l[i])
print("The values after l1 is created for below 100 values : ",l1)
