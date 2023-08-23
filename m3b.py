'''Write a Python program to append text to a file and 
display the text.'''
x=open('file.txt','r+')
x.write("This Is")
print(x.read())