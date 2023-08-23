"""Write a Python script to check if a given key already exists
 in a dictionary."""

dict1={'id':1,'name':'Rukhsar','sub':'python'}

chk=input("Enter The Key :")

if chk in dict1:
    print("Key Already Exist")
else:
    print("Key Is Not Exist")

