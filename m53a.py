#Q.	    How can you pick a random item from a list or tuple?
#Ans.   By using choice()

import random

list1=[1,2,3,4,5]
tuple1=(10,20,30,40,50)

print(f"This Is Random Function Using list :{random.choice(list1)}")
print(f"This Is Random Function Using Tupple :{random.choice(tuple1)}")