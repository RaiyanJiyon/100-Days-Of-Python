# Dictonary Methods

'''Dictionary uses several built-in methods for manipulation.They are listed below'''


#Update()

'''The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.'''

em1 = {
    1 : "Raiyan",
    2 : "Rajib",
    3 : "Rasel"
}

em2 = {
    4 : "Ishaq",
    5 : "Tamim",
    6 : "Akash"
}

em1.update(em2)
print(em1)

em1.update({1 : "Jiyon"})
print(em1)


#Removing items from dictionary:

'''There are a few methods that we can use to remove items from dictionary.

clear():
The clear() method removes all the items from the list.'''


print(em1.clear())


#pop():
'''The pop() method removes the key-value pair whose key is passed as a parameter.'''



info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)


#popitem()

'''The popitem() method removes the last key-value pair from the dictionary.'''

info.popitem()
print(info)


#del

'''we can also use the del keyword to remove a dictionary item.'''

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}

del info['DOB']
print(info)

'''If key is not provided, then the del keyword will delete the dictionary entirely.'''

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
# print(info)  -->> This line will throw error