#While loops

i=5
while i>0:
    print(i)
    i = i-1
else:
    print("Program Finished")


#Do while loop

number= int(input("Enter a Positive Number: "))
while True:
    print(number)
    if not number > 0:
        break
