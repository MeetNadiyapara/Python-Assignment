"""Write a Python function to get the largest number,
 smallest num and sum of all from a list."""
def list():
    ls=[25,35,15,65,45,55,75,85,95]
    print("Max:",max(ls))
    print("Min:",min(ls))
    print("Sum:",sum(ls))
list()    
#Using 'sort' function
"""list.sort()
print("Largest number is :",list[-1])
print("Smallest number is :",list[0])

total=sum(list)
print("sum of all numbers :",total)"""


#Sum of all the number by using for loop
"""
total=0
for i in range(0,len(list)):
    total=total+list[i]
print("sum of all numbers :"total)"""
