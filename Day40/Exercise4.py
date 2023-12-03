'''# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode'''


import random
import string

attempts = 0
max_attempts = 3
new_msg = None

while attempts < max_attempts:
    msg = input("Enter the message (at least 3 characters) for Encode: ")

    if len(msg) < 3:
        print("You have to enter at least 3 characters!")
        attempts += 1
    else:
        print("Your msg is ready for Encoding.")
        original_msg = msg
        first_character = original_msg[0]
        new_msg = original_msg[1:]
        new_msg += first_character
        random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        new_msg = random_chars + new_msg + random_chars
        break

if attempts == max_attempts:
    print("Program End.")

try:
    user_want1 = int(input("Do you want to see Encode version of your msg? Type 0 for No or Type 1 for Yes: "))
    if user_want1 not in (0, 1):
        raise ValueError("Invalid Input. Please enter either 0 or 1.")
    
    elif user_want1 in (0):
        print("Program End. Thank you.")
    
    elif user_want1 in (1):
         if new_msg is not None:
            print("Your Encode msg is: " + new_msg)

    
except ValueError as e:
    print(e)
    print("Program End Here. Thank You.")


# if user_want1 == 0:
#     print("Program End. Thank you.")
# else:
#     if new_msg is not None:
#         print("Your Encode msg is: " + new_msg)



