#Manipulating Tuples

tup = [10, 20, 30, 40, 50]

print(tup)

l = list(tup)

l.append(100)
l.pop(10)

tup = tuple(l)

print(tup)