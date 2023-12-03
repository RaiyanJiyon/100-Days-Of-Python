#readlines() method

'''The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.'''

f = open('student.txt', 'r')

# while True:
#     line = f.readline()
#     print(line)

#     if not line:
#         print("No Line left.")
#         break

'''he readlines() method reads all the lines of the file and returns them as a list of strings.'''

#writelines() method

'''The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

Here's an example of how to use the writelines() method:'''


# f2 = open('student3.txt', 'w')

# lines = ["Lines1,\nLines2,\nLines3"]

# f2.writelines(lines)
# f2.close()

'''Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:'''

# f2 = open('student3.txt', 'w')

# lines = ["Lines1", "Lines2", "Lines3"]

# for l in lines:
#     f2.write(l + '\n')

# f2.close()



f3 = open('student2.txt', 'r')

i = 0

while True:
    i += 1
    line4 = f3.readline()
    if not line4:
        print("No Student Mark Left.")
        break

    m1 = int(line4.split(",") [0])
    m2 = int(line4.split(",") [1])
    m3 = int(line4.split(",") [2])

    print(f"Student of {i} Bangla mark is: {m1}")
    print(f"Student of {i} Bangla mark is: {m2}")
    print(f"Student of {i} Bangla mark is: {m3}")