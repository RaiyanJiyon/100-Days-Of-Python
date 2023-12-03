#Python Class Methods

#Python Class Methods: An Introduction

class Employee:
    company = 'Apple'

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


#=============================================================================
e1 = Employee()
e1.name = "Harry"
e1.show()
e1.change_company("Tesla")
e1.show()
print(Employee.company) #it shows apple, because that methods is not a class method.
#But when we declare @classmethods decorator, it will shows Tesla.