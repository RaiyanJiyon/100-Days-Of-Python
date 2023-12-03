from typing import Any


class Employee:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    '''__str__ and __repr__ methods
    The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.'''

    def __str__(self) -> str:
        return f"Hello i am Str magic method."
    
    def __repr__(self) -> str:
        return f"Hello i am repr magic method."
    
    '''__call__ method
    The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create ob'''
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass