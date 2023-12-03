#Magic/Dunder Methods in Python

'''These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

Let's take a look at some of the most commonly used magic methods in Python.

__init__ method

'''

from emp import Employee

a1 = Employee("Raiyan", 23)

print(a1)