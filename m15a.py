# Write a Python program to get unique values from a list
a=[]

n=int(input("Enter Loop Elemnets:"))

for i in range(n):
    ent=input("Enter List Elements:")
    a.append(ent)

b=set(a)

print(list(b))