#Dictionary

'''Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.'''


student = {
    1 : "Raiyan",
    2 : "Rajib", 
    4 : "Akash",
    4 : "Surya", 
    5 : "Nehal", 
    6 : "Osama" 
}

print(student.keys())
print(student.values())
print(student.items())


#Accessing Dictionary items:

'''I. Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.'''


info = {'name':'Karan', 'age':19, 'eligible':True}

print(info['name'])
print(info.get('age'))


'''II. Accessing multiple values:
We can print all the values in the dictionary using values() method.'''


print(info.values())


'''III. Accessing keys:
We can print all the keys in the dictionary using keys() method.'''


print(info.keys())


'''IV. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.'''


print(info.items())


#Using Loop

info = {'name':'Karan', 'age':19, 'eligible':True, 101: 'Kabir'}

for key, values in info.items():
    print(f"Key : {key} and Value : {values}")