<h1>Day 5 - Comments, Escape sequence & Print in Python</h1>

<p>
Welcome to Day 5 of 100DaysOfCode. Today we will talk about Comments, Escape Sequences and little bit more about print statement in Python. We will also throw some light on Escape Sequences

<h3>Python Comments</h3>

A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

<h3>Single-Line Comments:</h3>
To write a comment just add a ‘#’ at the start of the line.

```python
#This is a 'Single-Line Comment'
print("This is a print statement.")
```

<h3>This is a print statement.</h3>


```python
print("Hello World !!!") #Printing Hello World
```

<h3>Output-</h3>
Hello World !!!

<h3>Multi-Line Comments:<h3>
To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

```python
#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```

<h3>Output</h3>
p is greater than 5.

<h3>Escape Sequence Characters</h3>

To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash \ followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

```python
print("This doesnt "execute")
print("This will \" execute")
```
</p>