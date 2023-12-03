#Match Statements

x = int(input("Enter your number: "))

match x:
    case 0:
        print("Number is Zero")
    case 1:
        print("Number is One")
    case _ if x!=10:
        print("Number is not 10")
    case _ if x!=100:
        print("Number is not 100")
    case _:
        print("Number is ",x)