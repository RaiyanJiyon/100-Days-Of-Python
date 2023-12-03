#Constructors

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} is a {self.age} years old.")

#===================================================================

a = Person("Raiyan Jiyon", 23)
a.info()


'''Types of Constructors in Python
1. Parameterized Constructor
2. Default Constructor'''