#Recursion in python

'''Factorail'''

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(3))
# print(factorial(5))


# nterm = int(input("Enter how many terms :"))

# first , second = 0 , 1

# count = 0
# if nterm <= 0:
#     print("Please Enter positive Number.")

# elif nterm == 1:
#     print(first)

# else:

#     while count < nterm:
#         print(first)

#         nth = first + second
#         first = second
#         second = nth
#         count += 1




# count = 0

# def fibo(n):

#     count = 0
#     n1 = 0
#     n2 = 1
#     if n <= 0:
#         print("Please Enter Positive Number: ")
    
#     elif n == 1:
#         print(n1)

#     else:
        
#         while count < n:

#             print(n1)

#             total = n1 + n2

#             n1 = n2
#             n2 = total

#             count += 1


# fibo(10)


'''With Recursion'''
        

def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo (n - 1) + fibo (n - 2)

print(fibo(5))