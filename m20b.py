'''Q.  Write python program that user to enter only odd numbers, else will
raise an exception.'''
try:
    ent=int(input("Enter Odd Number: "))
    mod = ent % 2
    if mod > 0:
        print("This is an odd number.")
except :
    print("This Number is Not Odd: ")
