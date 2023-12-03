#Exception Handling

try:
  num = int(input("Enter a Integer Number: "))

except ValueError:
    print("Not a Integer Number.")


try:
    print(f"Multiplication of {num} with 1 to 10: ")
    for i in range(1 , 11):
        print(f"{num} * {i} = {num * i}")

except:
    print("Invalid Input")

print("Program Finished.")