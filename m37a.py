"""	Write a Python script to print a dictionary where the keys 
are numbers between 1 and 15."""
dict1={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q'}
for i in range(1,16):
    print(i,':',dict1[i])


OR

l=int(input("Enter the Limit : "))
d = dict()
for x in range(1,l+1):
    d[x]=x**2
print(d)
    
        
