#The time Module in Python

import time

def WhileLoop():
    i = 0
    while i < 5000:
        i += 1
        print(i)
        

def ForLoop():
    for i in range(5001):
        print(i)

init = time.time()

WhileLoop()
t1 = time.time() - init
# print(t1)

ForLoop()
print(time.time() - init)
print(t1)