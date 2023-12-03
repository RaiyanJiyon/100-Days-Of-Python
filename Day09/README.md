<h1>Typecasting in python</h1>

<p>

The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

Python supports a wide variety of functions or methods like: <strong> int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict() </strong>, etc. for the type casting in python.

<h3>Two Types of Typecasting:</h3>

<ol>
<li>Explicit Conversion (Explicit type casting in python)</li>
<li>Implicit Conversion (Implicit type casting in python).</li>
</ol>

<h3>Explicit typecasting:</h3>

The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

It can be achieved with the help of Python’s built-in type conversion functions such as <strong>int(), float(), hex(), oct(), str() </strong>, etc .

<h3>Example of explicit typecasting:</h3>

```python
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
```

<h3> Output: </h3>
The Sum of both the numbers is 22


<h3> Implicit type casting: </h3>

Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.

<h3>Example of implicit type casting:</h3>

```python
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
```


<h3>Ouput: </h3>

<class 'int'> <br>
<class 'float'> <br>
10.0 <br>
<class 'float'> <br>

</p> 