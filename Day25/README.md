<h1>Manipulating Tuples</h1>

<p>Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.</p>

<h3>Example:</h3>

```python
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
```

<h3>Output:</h3>
('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
<br><br>

<p>Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

However, we can directly concatenate two tuples without converting them to list.</p>

<h3>Example:</h3>

```python
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
```

<h3>Output:</h3>
('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')

<h3>Tuple methods-</h3>

As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

<h3>count() Method-</h3>
The count() method of Tuple returns the number of times the given element appears in the tuple.

<h3>Syntax:</h3>
tuple.count(element)

<h3>Example</h3>

```python
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
```

<h3>Output</h3>
3

<h3>index() method-</h3>

The Index() method returns the first occurrence of the given element from the tuple.

<h3>Syntax:</h3>

```python
tuple.index(element, start, end)
```

<b>Note:</b> This method raises a ValueError if the element is not found in the tuple.

<h3>Example</h3>

```python
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
```

<h3>Output</h3>
3
