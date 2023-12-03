#Inheritance

'''When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

'''

class Employee:
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
    
    def details(self):
        print(f"{self.name} is a {self.age} years old.")

class manager(Employee):
    def language(self):
        print("Python")

#======================================================

e1 = Employee("Raiyan", 23)
e1.details()

m1 = manager("Jiyon", 24)
m1.language()


'''Types of inheritance:
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance'''