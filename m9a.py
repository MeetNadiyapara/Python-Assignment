""" 	Write a Python function that takes two lists and returns
 true if they have at least one common member."""
"""
def inp():
    ls1=[]
    ls2=[]
    n=input("Enter Number For Loop")    
    for i in n:
        lsfirst=(input("Enter first list Elements:"))
        lssecond=(input("Enter second list Elements:"))
        ls1.append(lsfirst)
        ls2.append(lssecond)

    ls1=set(ls1)
    ls2=set(ls2)

    c=ls1.union(ls2)

    ls1=list(ls1)
    ls2=list(ls2)

    if c:
        print(c)

    else:
        print(ls1)
        print(ls2)

inp()

"""
def inp():
    ls1=[]
    ls2=[]
    n=int(input("Enter Number For Loop:"))   
    for i in range(n):
        lsfirst=(input("Enter first list Elements:"))
        lssecond=(input("Enter second list Elements:"))
        ls1.append(lsfirst)
        ls2.append(lssecond)
    
    result='False'

    for i in ls1:
        for j in ls2:
            if i==j:
                result='True'

    print(ls1)
    print(ls2)
    
    print("The Answer Is",result)
inp()



