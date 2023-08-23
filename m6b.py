'''Write a Python program to read a file line by line and store it 
into a list'''
x=open('file.txt','r')
b=x.readline()
a=[]
a.append(b)
print(a)