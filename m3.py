#write a python program to get a fibonacci series of a given range.

d=int(input("enter:"))

a=0
b=1

'''print(a)
print(b)'''


for i in range(d):
    # b+=a
    print(a)
    a, b = b , a
    a += b


# a = a + b