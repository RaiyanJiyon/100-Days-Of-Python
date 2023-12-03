<h1>String Slicing & Operations on String
Length of a String </h1>

We can find the length of a string using <b>len()</b> function.

<h3>Example:</h3>

```python
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
```

<h3>Output:</h3>
Mango is a 5 letter word. <br>

<h3>String as an array</h3>

A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

<h3>Example:</h3>

```python
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index

```


<h3>Output:</h3>
Apple<br>
i  


<h3>Note:</h3> 

This method of specifying the start and end index to specify a part of a string is called slicing.

<h3>Slicing Example:</h3>

```python
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
```

<h3>Output:</h3>
Apple <br>
Pie <br>
pleP <br>
ApplePie <br>


<h3>Loop through a String:</h3>

Strings are arrays and arrays are iterable. Thus we can loop through strings.

<h3>Example:</h3>

```python
alphabets = "ABCDE"
for i in alphabets:
    print(i)
```

<h3>Output:</h3>
A <br>
B <br>
C <br>
D <br>
E <br>