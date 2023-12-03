#Lambda Functions in Python

#Normal Function

def avg(a, b):
    return (a + b) / 2

print(avg(10, 20))


'''In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:'''

x = lambda a, b : (a + b) / 2
print(x(5, 10))

y = lambda a, b, c : a + b + c

print(y(10, 20 , 30))


'''Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.'''


'''Lambda functions can have multiple arguments, just like regular functions. Here is an example of a lambda function with multiple arguments:'''

# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y

# Lambda function to calculate the product of two numbers
lambda x, y: x * y


# def fun(avg, value):
#     return avg(value) + 10

# print(fun(avg(10), 10))