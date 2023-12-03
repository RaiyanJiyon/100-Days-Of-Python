#Getter and Setter

'''Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:'''

class Fruit:

    def __init__(self, name : str):
        self._name = name

    '''This is normal way to make getter and setter method'''
    # def get_name(self):
    #     print("Getting name.")
    #     return self._name
    
    # def set_name(self, new_name : str):
    #     self._name = new_name

    '''This is professonal way to make getter and setter'''

    @property
    def fruit_name(self):
        print(f"{self._name} is accessed.")
        return self._name
    
    @fruit_name.setter
    def fruit_name(self,value):
        print(f"{self._name} is now {value}")
        self._name = value

    @fruit_name.deleter
    def fruit_name(self):
        print(f"{self._name} is now delete.")



if __name__ == '__main__':
    fruit = Fruit('Banana')
    # fruit.set_name("Orange")
    # print(fruit.get_name())

    print(fruit.fruit_name)

    fruit.fruit_name = "Orange"

    del fruit.fruit_name