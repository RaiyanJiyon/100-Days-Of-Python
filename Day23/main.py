#List Methods

l =[10,3,5,77,100,55,3]

print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l) 
'''The reverse parameter is set to False by default.

Note: Do not mistake the reverse parameter with the reverse method.

'''

#reverse()

'''This method reverses the order of the list.'''

colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

#index()

'''This method returns the index of the first occurrence of the list item.'''

nums = [10,3,5,77,100,55,3]
print(nums.index(10))

colors = ["voilet", "indigo", "blue", "green"]
print(colors.index('blue'))

#Count

'''Returns the count of the number of items with the given value.'''

nums = [10,3,5,77,100,55,3]
print(nums.count(3))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))


#Copy

'''Returns copy of the list. This can be done to perform operations on the list without modifying the original list.'''

num1 = nums.copy()
print(num1)

#append

'''This method appends items to the end of the existing list.'''

number = [10,3,5,77,100,55,3]
number.append(1000)
print(number)

colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)


#insert()

'''This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

'''

numbers = [10,3,5,77,100,55,3]
numbers.insert(1,200)
print(numbers)

#extend()

'''This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

'''


number.extend(numbers)
print(number)

#Concatenating two lists:

'''You can simply concatenate two lists to join two lists.'''

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)