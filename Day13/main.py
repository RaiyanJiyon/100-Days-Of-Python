#String methods

name= 'Raiyan'

'''The upper() method converts a string to upper case'''

print(name.upper())

'''The lower() method converts a string to lower case'''

print(name.lower())

'''The strip() method removes any white spaces before and after the string'''

str1 = ' Raiyan Jiyon'
print(str1)
print(str1.strip())

str2= 'Abdul Kalam!!'
print(str2.rstrip('!'))

'''The replace() method replaces all occurences of a string with another string'''

print(str2.replace('Abdul Kalam','Obaidul Kader'))

'''The split() method splits the given string at the specified instance and returns the separated strings as list items'''

str3= "Rajib Khan"
print(str3.split())

'''The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase'''

str4= "hello world"
print(str4.capitalize())

'''The center() method aligns the string to the center as per the parameters given by the user'''

str5= 'Hey World'
print(str5.center(50))

'''We can also provide padding character. It will fill the rest of the fill characters provided by the user'''

print(str5.center(50,'*'))

'''The count() method returns the number of times the given value has occurred within the given string'''

str6= 'Hello my name is Harry, and Harry is famous name'
print(str6.count('Harry'))
print(str6.count('harry')) #should be in same case, like upper or lower
print(str6.count('name'))

'''The endswith() method checks if the string ends with a given value. If yes then return True, else return False'''

print(str6.endswith('name'))
print(str6.endswith('harry'))

'''We can even also check for a value in-between the string by providing start and end index positions'''

print(str6.endswith('ell', 0, 10))

'''The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1'''

str7 = "He's name is Dan. He is an honest man."
print(str7.find('Dan'))

'''As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not'''
print(str7.find('jiyon'))

'''The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.'''

print(str7.index('Dan'))

'''As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not'''

'''The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False'''

print(str7.isalnum())

str8= "himynameisiyon8191H"
print(str8.isalnum())

'''The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False'''

str1 = "Welcome"
print(str1.isalpha())

'''The islower() method returns True if all the characters in the string are lower case, else it returns False'''

str9='raiyan jiyon'
print(str9.islower())

'''The isprintable() method returns True if all the values within the given string are printable, if not, then return False'''

str9='raiyan jiyon\n'
print(str9.isprintable())

'''The isspace() method returns True only and only if the string contains white spaces, else returns False'''

str10=' '
print(str10.isspace())

'''The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False'''

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

'''The endswith() method checks if the string starts with a given value. If yes then return True, else return False'''

str11= "I love python"
print(str11.endswith('python'))


'''The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case'''

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

'''The title() method capitalizes each letter of the word within the string'''

str12= 'hey my name is raiyan jiyon'
print(str12.title())