#Write a Python program to remove an empty tuple(s) from a list of tuples.
a=[('hii','hello'),(),('Python',1)]

for i in a:
    if i==():
        a.remove(i)
print(a)