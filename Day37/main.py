#Finally Clause

def func1():

    try:
        l = [1, 2 , 4, 7, 9]
        index = int(input("Enter the Index you want to see: "))

        print(l[index])
        return 1

    except IndexError as e:
        print(e)
        return 0

    except ValueError:
        print("Invalid Input.")
        return 0

    finally:
        print("Program Finished.")


num = func1()
print(num)
