# Write a Python program to read last n lines of a file.

f=open('file.txt','r')
print(f.readlines()[-1])