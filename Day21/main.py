#Function Arguments and return statement

'''There are four types of arguments that we can provide in a function:

Default Arguments
Keyword Arguments
Variable length Arguments
Required Arguments'''

#Default Argument

def average(a=20 , b=10):
    print("Average of given numbers: ", (a+b)/2)

average()

#Keyword Arguments

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")



#Required Arguments

def full_name(fname, mname, lname):
    print("Hello", fname , mname, lname)

full_name('MD', 'Raiyan', 'Jiyon')  #you have to must pass the given argument parameter while calling function



#Variable Length Arguments

'''There are two type of variable length arguments'''

'''Arbitrary Arguments'''


def average(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum + i
    print("Average of given  numbers are: ", sum/len(num))


average(10,20,30)


'''Keyword Arbitrary Arguments'''

# def name(**name):
#     print("Hello", name['fname'], name['mname'], name['lname'])


# name('MD', 'Raiyan', 'Jiyon')

def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")


#Return Statements

def average(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum + i
    average = sum / len(num)
    return average


c = average(10,20,30)
print(c)