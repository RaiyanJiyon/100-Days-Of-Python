# Super keyword in Python

'''The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

Here's an example of how to use the super() keyword in a simple inheritance scenario:'''

class Parent_Class:
    def parent_method(self):
        print("This is the parent method.")

class Child_Class(Parent_Class):

    def parent_method(self):
        print("This is the parent method by child class.")
        super().parent_method()
    

    def child_method(self):
        print("This is the child method.")



#==================================================

parent_object = Parent_Class()
parent_object.parent_method()

Child_object = Child_Class()
Child_object.child_method()
Child_object.parent_method()

print("\n\n")



'''Another Super keyword Example for constructor'''

class Employee:
    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age
    
    def display(self):
        print(f"{self.name} is a {self.age} years old.")

class Programmer(Employee):
    def __init__(self, name: str, age: int, language : str) -> None:
        super().__init__(name, age)
        self.language = language
    
    def display(self):
        print(f"{self.name} is a {self.age} years old and his programming language is {self.language}.")


rohan = Employee("Rohan", 23)
rohan.display()

harry = Programmer("Harry", 24, "Python")
harry.display()