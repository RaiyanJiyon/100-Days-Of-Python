<h1>List Methods</h1>

<h3>list.sort()</h3>

This method sorts the list in ascending order. The original list is updated

<h3>Example 1:</h3>

```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
```

<h3>Output:</h3>

['blue', 'green', 'indigo', 'voilet'] <br>
[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]


<b>What if you want to print the list in descending order? <br>
We must give reverse=True as a parameter in the sort method.</b>

<h3>Example:</h3>

```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
```

<h3>Output:</h3>

['voilet', 'indigo', 'green', 'blue'] <br>
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]


The reverse parameter is set to <b>False</b> by default.

<b>Note:</b> Do not mistake the reverse parameter with the reverse method.

<h3>reverse()-</h3>

This method reverses the order of the list.

<h3>Example:</h3>

```python
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
```

<h3>Output:</h3>

['green', 'blue', 'indigo', 'voilet']<br>
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]


<h3>index():</h3>

This method returns the index of the first occurrence of the list item.

<h3>Example:</h3>

```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
```

<h3>Output:</h3>

1 <br>
3 <br>

<h3>count():</h3>

Returns the count of the number of items with the given value.

<h3>Example:</h3>

```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
```

<h3>Output:</h3>
2 <br>
3 <br>

<h3>copy():</h3>

Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

<h3>Example:</h3>

```python
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)
```

<h3>Output:</h3>

['voilet', 'green', 'indigo', 'blue'] <br>
['voilet', 'green', 'indigo', 'blue']


<h3>append():</h3>
This method appends items to the end of the existing list.

<h3>Example:</h3>

```python
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)
```

<h3>Output:</h3>

['voilet', 'indigo', 'blue', 'green']


<h3>insert():</h3>

This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

<h3>Example:</h3>

```python
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]
colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]
print(colors)

```

<h3>Output:</h3>

['voilet', 'green', 'indigo', 'blue']


<h3>extend():</h3>

This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

<h3>Example 1:</h3

```python
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
```

<h3>Output:</h3>

['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']


<h3>Concatenating two lists:</h3>

You can simply concatenate two lists to join two lists.

<h3>Example:</h3>

```python
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
```


<h3>Output:</h3>

['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']