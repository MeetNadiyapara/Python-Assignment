"""
Write a python program to sum of the first n positive numbers
"""

a=int(input("Enter Number:"))
c=0

for i in range(a):
    i+=1
    c=c+i
print("Sum is:",c)