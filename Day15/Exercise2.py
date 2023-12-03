#Excersice 2: Good Morning Sir

'''Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.'''

import time

current_hour = int(time.strftime("%H"))

name= input("Enter Your Name: ")

if 5 <= current_hour < 12:
    print("Good Morning", name)

elif 12 <= current_hour < 17:
    print("Good Afternoon", name)

else:
    print("Good Evening", name)