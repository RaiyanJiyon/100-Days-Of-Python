#Raising custom errors in Python

# def voter(age):
#     if age < 18:
#         raise ValueError("Invalid Age.")
    
#     return "You are allowed for vote."


# try:
#     print(voter(9))
# except ValueError as e:
#     print(e)

# print("Program Finished.")


num = input("Enter any value between 5 and 9: ")

if num.lower() == "quit":
    print("Okay")
elif not num.isdigit():
    raise ValueError("Invalid input. Please enter a number.")
else:
    num = int(num)
    if num < 5 or num > 9:
        raise ValueError("Value should be in the range 5 to 9.")
    else:
        print("Valid input:", num)
