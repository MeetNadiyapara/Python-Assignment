#Write a Python program to check whether a list contains a sub list


main=[]
n=int(input("Enter Loop Elemnets:"))
for i in range(n):
    enter=input("Enter Main List Elements:")
    main.append(enter)
    sub=[]
for i in range(n):
    ent=input("Enter Sub List Elements:")
    sub.append(ent)
main.append(sub)   
    
print(main)

if sub in main:
    print("True")
else:
    print("False")




            




        
    