<h1>Python Tuples</h1>
<p>Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.</p>

<h3>Example 1:</h3>

```python
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
```


<h3>Output:</h3>
(1, 2, 2, 3, 5, 4, 6)<br>
('Red', 'Green', 'Blue')


<h3>Example 2:</h3>

```python
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
```

<h3>Output:</h3>
('Abhijeet', 18, 'FYBScIT', 9.8)

<h1>Tuple Indexes</h1>
<p>Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.</p>

<h3>Example:</h3>

```python
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]
```

<h3>Accessing tuple items:</h3>

<b>I. Positive Indexing:</b>

As we have seen that tuple items have index, as such we can access items using these indexes.

<h3>Example:</h3>

```python
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]     
print(country[0])
print(country[1])
print(country[2])
```

<h3>Output:</h3>

Spain<br>
Italy<br>
India<br>

<b>II. Negative Indexing:</b>

<p>Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.<p>

<h3>Example:</h3>

```python
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])
```

<h3>Output:</h3>

Germany<br>
India</br>
Italy</br>

<b>III. Check for item:</b>

We can check if a given item is present in the tuple. This is done using the in keyword.

<h3>Example 1:</h3>

```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
```

<h3>Output:</h3>

Germany is present.

<h3>Example 2:</h3>

```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
```

<h3>Output:</h3>

Russia is absent.


<h3>IV. Range of Index:</h3>

You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

<h3>Syntax:</h3>

Tuple[start : end : jumpIndex]


<b>Note:</b> jump Index is optional. We will see this in given examples.

<h3>Example: Printing elements within a particular range:</h3>

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
```

<h3>Output:</h3>
('mouse', 'pig', 'horse', 'donkey')<b>
('bat', 'mouse', 'pig', 'horse', 'donkey')<b>


<p>Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values. Note: The element of the end index provided will not be included.</p>

<h3>Example: Printing all element from a given index till the end</h3>

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes
```

<h3>Output:</h3>

('pig', 'horse', 'donkey', 'goat', 'cow')<br>
('horse', 'donkey', 'goat', 'cow')<br>


When no end index is provided, the interpreter prints all the values till the end.

<h3>Example: printing all elements from start to a given index</h3>

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes
```

<h3>Output:</h3>

('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')<br>
('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')<br>


<p>When no start index is provided, the interpreter prints all the values from start up to the end index provided.</p>

<h3>Example: Print alternate values</h3>

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
```

<h3>Output:</h3>
('cat', 'bat', 'pig', 'donkey', 'cow')
('dog', 'mouse', 'horse', 'goat')


<p>Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.</p>

<h3>Example: printing every 3rd consecutive withing given range</h3>

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])
```

<h3>Output:</h3>
('dog', 'pig', 'goat')


Here, jump index is 3. Hence it prints every 3rd element within given index.