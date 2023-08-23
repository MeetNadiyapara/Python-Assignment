"""	Write a Python function to reverses a string if its length 
is a multiple of 4."""

def lenth():
    m=input("Enter The Word Multiply By 4:")
    n=input("Enter The Word:")

    if len(m) % 4 == 0:
        for i in reversed(m):
            #print(m)
            print(i)
           


    elif  len(n) % 4 == 0:
        for j in reversed(n):
            n==0
        print(j)

    else:
        print("First String:",m)
        print("Second String:",n)
        
lenth()
