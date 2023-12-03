#Enumerate function in python


'''This is Normal Way'''
marks = [10, 20, 50, 89, 98, 100, 55]
index = 0
for mark in marks:
    print(mark)

    if index == 4:
        print("Harry Awesome") 
    index += 1


'''This is Enumerate Function'''

for index, mark in enumerate(marks):
    print(mark)

    if index == 4:
        print("I am Awesome")

'''We can also define index starting point with (start) varaible like this.'''
for index, mark in enumerate(marks, start = 1):
    print(mark)

    if index == 4:
        print("We are Awesome")