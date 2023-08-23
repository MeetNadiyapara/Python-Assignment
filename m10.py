"""
Write a python program that will return true if the two given integer
values are same or their sum or difference is 5.
"""

a=int(input("First value :"))
b=int(input("Second value :"))

m=a-b

if m==5:
    print("Difrence")

elif a==b:
    print("Equal")
