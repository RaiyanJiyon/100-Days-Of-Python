'''1. Calculate the Factorial of a Number:
Write a Python function that calculates the factorial of a given positive integer.'''


def Factorial(num):
    fact = 1
    if num<0:
        print("Sorry..! Negative numbers factorials are not exist.")
    elif num == 0:
        print("Factorial of number 0 is 1")
    else:
        for i in range(1, num + 1):
            fact = fact * i
        print(f"Factorial of {num} is {fact}")


num = int(input("Enter any integer number: "))

Factorial(num)