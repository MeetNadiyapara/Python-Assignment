""" Write a Python function that takes a list and returns
 a new list with unique elements of the first list."""
def lis():
    ls=[]
    ls1=[]
    n=int(input("Enter Value Greater Than 5:"))
    for i in range(n):
        list1=int(input("Enter First List Value:"))
        ls.append(list1)
        ls1.append(list1) 
    print(ls)
    c=set(ls1)
    d=list(c)
    print(d)
lis()
 
OR

list=[1,3,2,5,2,3,23,1,2,5,7]
unique_list=[]
for a in list:
    if a not in unique_list:
        unique_list.append(a)

print(unique_list)

    
