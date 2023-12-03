#Function catching in Python

from functools import lru_cache
import time

@lru_cache(maxsize = None)
def fx(n):
    time.sleep(5)
    return n * 5


print(fx(5))
print("Done for 5.")

print(fx(15))
print("Done for 15.")

print(fx(25))
print("Done for 25.")

#Same value again 

print(fx(5))
print("Done for 5.")

print(fx(15))
print("Done for 15.")

print(fx(25))
print("Done for 25.")