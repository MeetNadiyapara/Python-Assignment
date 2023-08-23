# Write a Python program to count the frequency of words in a file.
x=open('student_data.txt','r')

for mystr in x:
    a=mystr.count('Meet')
print(a)