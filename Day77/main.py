#Operator Overloading in Python: An Introduction

'''Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.'''

#Why do we need operator overloading?

'''Operator overloading allows you to create more readable and intuitive code. For instance, consider a custom class that represents a point in 2D space. You could define a method called 'add' to add two points together, but using the + operator makes the code more concise and readable:'''

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.a + other.a, self.b + other.b)
        else:
            raise TypeError("Unsupported operand type for +: Point and {}".format(type(other)))

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.a, p3.b)  # prints 4, 6


#How to overload an operator in Python?

'''You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). Here are some of the most commonly overloaded operators and their corresponding special methods:
+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__
'''