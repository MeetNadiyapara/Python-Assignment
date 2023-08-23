"""•	Write a Python function to calculate the factorial of 
a number (a nonnegative integer)"""
def cal():
    a=int(input("Enter Number : "))
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact)
cal()