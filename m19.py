""" 
Write a Python program to find the first appearance of the 
substring 'not' and 'poor' from a given string, if 'not' follows 
the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Return the resulting string.  
"""

a="Anil Ambani Is India'st Richest Guy , And He Is Not Poor"

b=a.find("Not")

d=a.find("Poor")

#c=a.replace("Not Poor","Good")
c=a.replace((a[b:d+4]),"Good")

print(c)