"""     Write a Python program to add 'ing' at the end of a given string
(length should be at least 3). If the given string already ends with
'ing' then add 'ly' instead if the string length of the given string
is less than 3, leave it unchanged.     """


a=input("Enter Atleast 3 Character:")
if len(a)>=3:
    a += 'ing'
    print(a)
    
    b=input("Enter Any Charachter Which Does Not End With ing:")
    b += 'ing'
    print(b)

    c=input("Enter Any Charachter Which End With ing:")
    c += 'ly'
    print(c) 

else:
    print(a)