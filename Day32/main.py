#Joining Sets

#I. union() and update():

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities1.union(cities2))

cities3= {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities4 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3.update(cities4)
print(cities3)


#II. intersection and intersection_update():

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.intersection(cities2)
print(cities3)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.intersection_update(cities2)
print(cities1)


#III. symmetric_difference and symmetric_difference_update():


num1 = {1,2,3,4,5,6}
num2 = {7,8,9,1,1,2}

print(num1.symmetric_difference(num2))

num1.symmetric_difference_update(num2)
print(num1)


#IV. difference() and difference_update():

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

'''Difference methods'''
print(cities.difference(cities2))


#isdisjoint():

'''The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

'''


c1 =  {'Dhaka', "Sylhet", 'Comilla'}
c2 =  {'Dhaka', "Sylhet", 'Comilla'}

print(c1.isdisjoint(c2))


#issuperset():

'''The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
'''

print(c1.issuperset(c2))


#issubset():

'''The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
'''

print(c1.issubset(c2))


#add()

'''If you want to add a single item to the set use the add() method'''

c1.add("Rajshahi")
print(c1)


#Update()

'''If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)


#remove()/discard()

'''We can use remove() and discard() methods to remove items form list.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

'''The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.'''



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Toko")
print(cities)


#Pop()

'''This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#del

'''del is not a method, rather it is a keyword which deletes the set entirely.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
#print(cities)


#Clear()

'''This method clears all items in the set and prints an empty set.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)


#Check if item exists

'''You can also check if an item exists in the set or not.'''


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

if "Tokyo" in cities:
    print("Tokya in the Set")

else:
    print("Tokya is not in the Set")