"""Write a Python program to count the number of strings
where the string length is 2 or more and the first and last
character are same from a given list of strings."""

str='eye','php','java','python'
c=0
for str in str:
    if len(str)>1 and str[0]==str[-1]:
        c+=1
    
print(c)
