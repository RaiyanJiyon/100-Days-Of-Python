'''
Password Validation: Create a Python program that repeatedly asks the user for a password until they enter the correct password. Use a while loop and the break statement to exit the loop when the correct password is entered.
'''

set_password= input("Set your password: ")

print("Log In: ")

attemp = 0
max_attemp = 5

while attemp < max_attemp:
    check_password = input("Enter your password: ")
    if set_password == check_password:
        print("Welcome in your Account.")
        break
    else:
        print("Wrong Password.!! Try Again.")
        attemp += 1
        if attemp == max_attemp:
            print("Sorry, your password trial is over.")
            
print("Program Finished")


