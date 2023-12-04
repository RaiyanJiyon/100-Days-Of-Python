'''3. Reverse a String:
Write a function that reverses a given string.'''

def reverse_string(name):
    reverse_name= name [:: -1]
    print(reverse_name)

name = input("Enter your name: ")

reverse_string(name)