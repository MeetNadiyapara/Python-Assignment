"""•	Write a Python program to get a single string from two given
 strings, separated by a space and swap the first two characters 
 of each string."""



a=input("Enter first line :")

b=input("Enter second line :")

print(a.replace(a[0:2],b[0:2]),b.replace(b[0:2],a[0:2]))

