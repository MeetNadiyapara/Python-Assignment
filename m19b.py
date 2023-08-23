'''Q.  How Do You Handle Exceptions With Try/Except/Finally In Python?
Explain with coding snippets.'''

try:
    ent=int(input("Enter Number: "))
    print(ent*ent)
except Exception as a:
    print("You Enter Invalid Input") and print(a)
finally:
    print("Finally Block Always Excecute")
