
from functools import reduce
import functools

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
"""
def lambda1(x):
    if (x % 2 != 0):
        return x
        filiter --> list object  
        map --> performs operation on each element and return all elements
        
        reduce --> single element
        """

# synrax list/(method_name(lambda returned value: conditon , input_list
final_list = list(filter(lambda x: (x % 2 != 0), li)) # x is list iteration variable
print(final_list)


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)

lis = [1, 3, 5, 6, 2, -342]

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a < b else b, lis))