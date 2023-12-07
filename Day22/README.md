<h1>Python Lists</h1>

<ul>
<li>Lists are ordered collection of data items.</li>
<li>They store multiple items in a single variable.</li>
<li>List items are separated by commas and enclosed within square brackets [].</li>
<li>Lists are changeable meaning we can alter them after creation.</li>
</ul>

<h3>Example 1:</h3>

```python
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
```

<h3>Output:</h3>

[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']


<h3>Example 2:</h3>

```python
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
```

<h3>Output:</h3>

['Abhijeet', 18, 'FYBScIT', 9.8]

As we can see, a single list can contain items of different data types.

<br>

<h1>List Indexing</h1>

<p>Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], the second item has index [1], the third item has index [2], and so on.</p>

<h3>Example:</h3>

```python
    colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#              [0]      [1]     [2]      [3]      [4]</code></pre>
```

<p><strong>Accessing list items</strong></p>

<p>We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...</p>

<h4>Positive Indexing:</h4>

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
```


<strong>Output:</strong>

Blue
Green
Red

<h4>Negative Indexing:</h4>

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])
```

<strong>Output:</strong>

Green
Blue
Red

<strong>Check whether an item is present in the list?</strong>

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
```

<strong>Output:</strong>

Yellow is present.

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")
```

<strong>Output:</strong>

Orange is absent.


<strong>Range of Index:</strong>

<p>You can print a range of list items by specifying where you want to start, where you want to end, and if you want to skip elements in between the range.</p>

<h4>Syntax:</h4>

```python
listName[start : end : jumpIndex]
```


<h1>List Comprehension</h1>

<p>List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.</p>

<h3>Syntax:</h3>

```python
List = [Expression(item) for item in iterable if Condition]

```

<strong>Expression:</strong> It is the item which is being iterated.
    
<strong>Iterable:</strong> It can be a list, tuple, dictionary, set, or even an array or string.

<strong>Condition:</strong> Condition checks if the item should be added to the new list or not.

<h3>Example 1:</h3>

```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
```

<strong>Output:</strong>

['Milo', 'Bruno', 'Rosa']

<h3>Example 2:</h3>

```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
```

<strong>Output:</strong>

['Sarah', 'Bruno', 'Anastasia']
