# Write a python program to find the longest words.

a=input("Enter String : ")
b=a.split()
e=max(b)
c=[]
for i in b:
    c.append(len(i))
print(max(c))
print("Longest Word:",e)
