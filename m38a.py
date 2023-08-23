# Write a Python program to check multiple keys exists in a dictionary...

dict1={1:'hello',2:'python',3:'java',4:'swift'}

#print("Multiple Key Is Available",dict1.keys()>{1,3})
#print("Multiple Key Is Available",dict1.keys()>{6,7})
ent=int(input("Enter Value :"))

if ent in dict1:
    print("Key Available")
else:
    print("Key Not Available")