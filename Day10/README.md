<h1>Day 10 - Taking User Input in python</h1>

<p>
In python, we can take user input directly by using <strong>input()</strong> function.This input function gives a return value as string/character hence we have to pass that into a variable

<h3>Syntax: </h3>

```python
variable=input()

```

But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

<h3> Example: </h3>

```python
variable=int(input())
variable=float(input())
```

We can also display a text using input function. This will make input() function take user input and display a message as well

<h3>Example: </h3>

```python
a=input("Enter the name: ")
print(a)
```

<h3>Output: </h3>
Enter the name: Harry <br>
Harry

</p>