'''
FizzBuzz with Continue: Implement the FizzBuzz game in Python using a for loop that iterates from 1 to 100. However, when a number is divisible by 3 or 5, instead of printing "Fizz" or "Buzz," use the continue statement to skip printing that number.
'''

for num in range(1,101):
    if num % 3 == 0 or num % 5 == 0:
        continue
    else:
        print("Fiz-Number",num)