""" Write a Python script to sort (ascending and descending) a 
dictionary by value.    """
import operator

d={'python':95,'java':85,'php':88}
print("Original order of dictionary :",d)

assending=dict(sorted(d.items(),key=operator.itemgetter(1)))
print("Assending Order Dictonary :",assending)

dessending=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=(1)))
print("Dessending Order Dictonary :",dessending)