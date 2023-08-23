"""Write a python program that swap two numbers with temp variable and 
without temp variable"""

a=int(input("Enter Value A:"))
b=int(input("Enter Value B:"))
temp=a
a = b
b = temp
print("Value of A:",a)
print("Value of B:",b)

