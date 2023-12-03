<h1>String methods</h1>

Python provides a set of built-in methods that we can use to alter and modify the strings.

<h3>upper() :</h3>
The <b>upper()</b> method converts a string to upper case.

<h3> Example:</h3>

```python
str1 = "AbcDEfghIJ"
print(str1.upper())

```

<h3>Output:</h3>

ABCDEFGHIJ


<h3>lower() :</h3>

The lower() method converts a string to lower case.

<h3>Example:</h3>

```python
str1 = "AbcDEfghIJ"
print(str1.lower())
```

<h3>Output:</h3>
abcdefghij


<h3>strip() :</h3>

The <b>strip()</b> method removes any white spaces before and after the string.

<h3>Example:</h3>

```python
str2 = " Silver Spoon "
print(str2.strip)
```

<h3>Output:</h3>
Silver Spoon


<h3> rstrip() :</h3>
the <b>rstrip()</b> removes any trailing characters. 

<h3>Example:</h3>

```python
str3 = "Hello !!!"
print(str3.rstrip("!"))

```

<h3>Output:</h3>

Hello


<h3>replace() :</h3>
The <b>replace()</b> method replaces all occurences of a string with another string. Example:

```python
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

```

<h3>Output:</h3>
Silver Moon


<h3>split() :</h3>
The split() method splits the given string at the specified instance and returns the separated strings as list items.

<h3>Example:</h3>

```python
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
```

<h3>Output:</h3>
['Silver', 'Spoon']

<br>
There are various other string methods that we can use to modify our strings.

<h3>capitalize() :</h3>
The <b>capitalize()</b> method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

<h3>Example:</h3>

```python
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
```

<h3>Output:</h3>
Hello <br>
Hello world <br>

<h3>center() :</h3>

The <b>center()</b> method aligns the string to the center as per the parameters given by the user.

<h3>Example:</h3>

```python
str1 = "Welcome to the Console!!!"
print(str1.center(50))
```

<h3>Output:</h3>
            Welcome to the Console!!! <br>


We can also provide padding character. It will fill the rest of the fill characters provided by the user.

<h3>Example:</h3>

```python
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))
```



<h3>Output:</h3>
............Welcome to the Console!!!.............


<h3>count() :</h3>
The <b>count()</b> method returns the number of times the given value has occurred within the given string.

<h3>Example:</h3>

```python
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
```



<h3>Output:</h3>
4


<h3>endswith() :</h3>
The <b>endswith()</b> method checks if the string ends with a given value. If yes then return True, else return False.

<h3>Example :</h3>

```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
```

<h3>Output:</h3>
True

<br>

We can even also check for a value in-between the string by providing start and end index positions.

<h3>Example:</h3>

```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
```



<h3>Output:</h3>
True


<h3>find() :</h3>

The <b>find()</b> method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

<h3>Example:</h3>

```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

```

<h3>Output:</h3>
10
<br>

As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

<h3>Example:</h3>

```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))
```


<h3>Output:</h3>
-1


<h3>index() :</h3>
The <b>index()</b> method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

<h3>Example:</h3>

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
```


<h3>Output:</h3>
13


As we can see, this method is somewhat similar to the <b>find()</b> method. The major difference being that index() raises an exception if value is absent whereas find() does not.

<h3>Example:</h3>

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))
```


<h3>Output:</h3>
ValueError: substring not found


<h3>isalnum() :</h3>
The <b>isalnum()</b> method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

<h3>Example 1:</h3> 

```python
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
```


<h3>Output:</h3>

True


<h3>isalpha() :</h3>

The <b>isalnum()</b> method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

<h3>Example :</h3>

```python
str1 = "Welcome"
print(str1.isalpha())
```


<h3>Output:</h3>
True


<h3>islower() :</h3>
The <b>islower()</b> method returns True if all the characters in the string are lower case, else it returns False.

<h3>Example:</h3>

```python
str1 = "hello world"
print(str1.islower())
```


<h3>Output:</h3>
True


<h3>isprintable() :</h3>
The <b>isprintable()</b> method returns True if all the values within the given string are printable, if not, then return False.

<h3>Example :</h3>

```python
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
```

<h3>Output:</h3>
True


<h3>isspace() :</h3>
The <b>isspace()</b> method returns True only and only if the string contains white spaces, else returns False.

<h3>Example:</h3>

```python
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
```


<h3>Output:</h3>
True <br>
True <br>


<h3>istitle() :</h3>
The <b>istitile()</b> returns True only if the first letter of each word of the string is capitalized, else it returns False.

<h3>Example:</h3>

```python
str1 = "World Health Organization" 
print(str1.istitle())
```

<h3>Output:</h3>
True


</h3>Example:</h3>

```python
str2 = "To kill a Mocking bird"
print(str2.istitle())
```



<h3>Output:</h3>
False


<h3> isupper() : </h3>
The <b>isupper()</b> method returns True if all the characters in the string are upper case, else it returns False.

<h3>Example :</h3>

```python
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

```

<h3>Output:</h3>
True


<h3>startswith() :</h3>
The <b>endswith()</b> method checks if the string starts with a given value. If yes then return True, else return False.

<h3>Example :</h3>

```python
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

```


<h3>Output:</h3>
True


<h3>swapcase() :</h3>
The <b>swapcase()</b> method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

<h3>Example:</h3>

```python
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
```

<h3>Output:</h3>
pYTHON IS A iNTERPRETED lANGUAGE


<h3>title() :</h3>
The <b>title()<b> method capitalizes each letter of the word within the string.

<h3>Example:</h3>

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())

```

<h3>Output:</h3>
He'S Name Is Dan. Dan Is An Honest Man.