#Python Class and Objects

'''A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.'''

class Person:
    name = "Harry"
    occupation = "CSE Lecturer"
    net_worth = 1000

    def info(self):
        print(f"{self.name} is a {self.occupation} and his net worth is {self.net_worth}")

#=========================================================

a = Person()
a.info()

b = Person()
b.name = "Jiyon"
b.occupation = "CSE Student"
b.net_worth = 0
b.info()

c = Person()
c.name = "Rajib"
# c.occupation = "CSE Student"
c.net_worth = 200
c.info()


#self parameter

'''The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition'''