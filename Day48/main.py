#local and global variables

x = 10 # this is global variable

def hello():
    '''For testing local variable'''
    global x 
    x = 50

    y = 20 #this is local variable
    print("Value Of Y: ",y)

hello()

print("Value Of X: ",x)
