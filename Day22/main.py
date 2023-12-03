#Python Lists

lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)


#List Index

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

print(colors)
print(colors[:])
print(colors[0:-1])
print(colors[0: len(colors) - 1])

if 'Red' in colors:
    print("Yes")
else:
    print("No")

if 'White' in colors:
    print("Yes")
else:
    print("No")


#Range of Index:

'''listName[start : end : jumpIndex]'''

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes


#List Comprehension

'''List = [Expression(item) for item in iterable if Condition]'''

nums= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [item for item in nums if item % 2 == 0]
print(numbers)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)