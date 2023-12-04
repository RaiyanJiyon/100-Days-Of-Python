'''2. Check for Prime Numbers:
Write a function that checks if a given number is prime.'''

def isPrime(num):

    flag = False

    if num < 0:
        print("Prime number not exist in negative number.")
    elif num == 0 or num == 1:
        print("Not a Prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
        if flag:
            print(f"Given {num} is not a prime number")
        else:
            print(f"Given {num} is a Prime number")
 

num = int(input("Enter positive number: "))

isPrime(num)