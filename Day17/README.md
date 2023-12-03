<h1>Introduction to Loops</h1>

Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

<b>for loop <br>
while loop <br>
The for Loop </b> 

</br>

for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

<h3>Example: iterating over a string:</h3>

```python
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```


<h3>Output:</h3>
A, b, h, i, s, h, e, k,

<br>

<h3>Example: iterating over a list:</h3>

```python

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
```


<h3>Output:</h3>
Red <br>
Green <br>
Blue <br>
Yellow

<br>
Similarly, we can use loops for lists, sets and dictionaries.

<h3>range():</h3>

What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

<h3>Example:</h3>

```python
for k in range(5):
    print(k)
```

<h3>Output:</h3>
0 <br>
1 <br>
2 <br>
3 <br>
4 

<br>

Here, we can see that the loop starts from 0 by default and increments at each iteration.

But we can also loop over a specific range.

<h3>Example:</h3>

```python
for k in range(4,9):
    print(k)
```

<h3>Output:</h3>

4 <br>
5 <br>
6 <br>
7 <br>
8

<br>

<h3>Quick Quiz</h3>

Explore about third parameter of range (ie range(x, y, z))