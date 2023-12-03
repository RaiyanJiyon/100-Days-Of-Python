#Opening a File


# file = open('student.txt', 'r')
# # print(file.readable())

# text = print(file.read())
# file.close()


#Modes in file


'''1. read mood'''
'''2. write mood'''
'''3. append mood'''

file2 = open('student2.txt', 'w')

text2 = file2.write("Hello my name is Khan.")

file2.close()

file2 = open('student2.txt', 'a')

text2 = file2.write("\nand i am 23 years old.")

file2.close()


'''4. create (x) mood'''


'''5. text (t) mood'''

#Reading from a File

f = open('student.txt', 'r')
contents = f.read()
print(contents)


#The 'with' statement

with open('student.txt', 'r') as file:
   print(file.read())  #Now we don't need to be closed this file.