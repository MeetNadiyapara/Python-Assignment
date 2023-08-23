""" 	Write a Python function that takes a list of words and returns
 the length of the longest one."""

def list():
    ls=[]

    m=int(input("Enter The Number Of word:"))

    for i in range(m):
        n=input("Enter The word:")
        ls.append(n)
        print("Lenghth Of The Word:",len(n))
    print(ls)

    print("Longest Lenth Of word",len(min(ls)))
   
         

    """n=('hi','hello','hey')
    ls.append(n)
    print(len(n[1]))"""

list()

