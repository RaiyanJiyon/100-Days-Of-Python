#Method Overriding in Python

'''Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is {self.age} years old.")

class Teacher(Person):
    def __init__(self, name, age, cgpa):
        super().__init__(name, age)
        self.cgpa = cgpa

    def display(self):
        super().display()  # Call the display method of the parent class
        print(f"His CGPA is {self.cgpa}.")

# Create instances of the classes
person = Person("Alice", 30)
teacher = Teacher("Bob", 35, 3.8)

# Call the display method for both objects
person.display()
teacher.display()

'''In conclusion, method overriding is a powerful feature in Python that allows you to customize the behavior of a class based on its specific needs. By using method overriding, you can create more robust and reliable code, and ensure that your classes behave in the way that you need them to. Additionally, by using the super function, you can extend the behavior of a base class method, rather than replace it, giving you even greater flexibility and control over the behavior of your classes.'''