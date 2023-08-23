"""•	Write a Python program to combine two dictionary adding values
 for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).
"""

dict1 = {'a': 100, 'b': 200, 'c':300}  
dict2 = {'a': 300, 'b': 200, 'd':400}  
new_dict = dict2  
for i, j in dict1.items():  
    if i in dict2:  
        new_dict[i] = j + dict2[i]  
    else:   
        new_dict[i] = j  
print("The new dict is:", new_dict) 

"""

from collections import Counter

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d=Counter(d1)+Counter(d2)
print(d)"""