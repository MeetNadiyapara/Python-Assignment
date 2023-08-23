""" 	Write a Python program to generate and print a list
 of first and last 5 elements where the values are square of 
 numbers between 1 and 30.
"""


ls1=[]
ls2=[]
n=int(input("Enter Value:"))
for i in range(n):
        list1=int(input("Enter First List Value:"))
        if list1<30:
            d=list1*list1
            ls1.append(d)
        else:
             ls1.append("Your Value Is Greater than 30")
             

for j in range(n):   
    list2=int(input("Enter Second List Value:"))
    if list2<30:  
        c=list2*list2
        ls2.append(c)
    else:
        ls2.append("Your Value Is Greater than 30")

print(ls1)
print(ls2)
    

