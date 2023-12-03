#Map, Filter and Reduce

'''In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments'''


'''Normal Way'''

def cube(x):
    return x*x*x

items = [10, 20, 4, 6, 5, 4]

newitem = []

for item in items:

    newitem.append(cube(item))

print(newitem)


#MAP

'''Same Program With MAP'''

newitem = list(map(cube, items))

print(newitem)


# FILTER

def FILTER(a):
    return a>4

newfilter = list(filter(FILTER, items))

print(newfilter)


# REDUCE 

from functools import reduce

numbers = [1, 3, 4, 6, 7, 8]

y = reduce(lambda x, y: x + y , numbers)

print(y)