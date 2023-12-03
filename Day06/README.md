<h1>Day 6 - Variables and Data Types </h1>

<p>
<h3>What is a variable?</h3>

Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

```python
a = 1
b = True
c = "Harry"
d = None
```

These are four variables of different data types.

<h3>What is a Data Type?</h3>

Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error. <br>

In python, we can print the type of any operator using type function:

```python
a = 1
print(type(a))
b = "1"
print(type(b))
```

By default, python provides the following built-in data types:

<h2>1. Numeric data: int, float, complex</h2>

<ul>
<li>int: 3, -8, 0</li>
<li>float: 7.349, -9.0, 0.0000001</li>
<li>complex: 6 + 2i</li>
</ul>
<br>

<h2>2. Text data: str</h2>

str: "Hello World!!!", "Python Programming"

<h2>3. Boolean data:</h2>
Boolean data consists of values True or False.

<h2>4. Sequenced data: list, tuple </h2>
<h3> list: </h3> 
A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

<h3> Example: </h3>

```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```

<h3> Output: </h3>

[8, 2.3, [-4, 5], ['apple', 'banana']]


<h3> Tuple: </h3> 
A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

<h3> Example: </h3>

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```

<h3> Output: </h3>

(('parrot', 'sparrow'), ('Lion', 'Tiger'))


<h2>5. Mapped data: dict</h2>

<h3> dict: </h3> 
A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

<h3> Example: </h3>

```python
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)

```

<h3> Output: </h3>

{'name': 'Sakshi', 'age': 20, 'canVote': True}

</p>