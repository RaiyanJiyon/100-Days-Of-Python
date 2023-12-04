'''
Prime Number Checker: Write a Python program that takes an integer input from the user and uses a for loop to determine if it's a prime number. If the number is not prime, exit the loop early using the break statement.
'''

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    elif number == 2:
        return True  # 2 is a prime number

    # Check for divisibility by numbers from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible by 'i', so it's not prime
    return True

# Input from the user
user_input = int(input("Enter an integer: "))

# Check if the input is prime
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")



