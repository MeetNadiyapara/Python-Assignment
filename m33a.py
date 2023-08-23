""" Write a Python script to concatenate following dictionaries 
to create a new one."""
dict1={1:2,2:3}
dict2={3:4,4:5}
dict3={5:6,6:7}
dict4={}  
for i in dict1,dict2,dict3:
    dict4.update(i)
print(dict4)

#print(dict4.update(dict1,dict2,dict3))