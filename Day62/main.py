# #Access Specifiers/Modifiers

# '''Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
# '''

# '''Types of access specifiers
# Public access modifier
# Private access modifier
# Protected access modifier'''

# #Public 

# class Employee:
#     def __init__(self) -> None:
#         self.name = "Harry"


# a = Employee()
# print(a.name)


# #Private

# class Employee:
#     def __init__(self) -> None:
#         self.__name = "Harry"


# a = Employee()
# print(a._Employee__name)
# print(a.__dir__())

'''Name Mangling'''

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute


'''Protected'''
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())