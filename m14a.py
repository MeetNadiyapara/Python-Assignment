# Write a Python program to find the second smallest number in a list
a=[]

n=int(input("Enter Loop Elemnets:"))

for i in range(n):
    ent=input("Enter List Elements:")
    a.append(ent)

a.sort()
print(a)
print(a[1])