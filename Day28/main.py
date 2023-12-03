#String formatting in python

'''Old way to use'''

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

'''New way'''

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")


'''We can use it in a single statement as well.'''

print(f"{2 * 30}")