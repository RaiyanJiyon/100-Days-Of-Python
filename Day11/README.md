<h1>What are strings?</h1>

<p>
In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

<h3>Example-</h3>

```python
name = "Harry"
print("Hello, " + name)
```

<h3>Output-</h3>
Hello, Harry <br>


<h3>Note:</h3> 
It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience

```python
print('He said, "I want to eat an apple".')

```


<h3>Multiline Strings-</h3>

If our string has multiple lines, we can create them like this:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

```


<h3>Accessing Characters of a String-</h3>

In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.

```python
print(name[0])
print(name[1])

```

<h3>Looping through the string-</h3>

We can loop through strings using a for loop like this:

```python
for character in name:
    print(character)
```

Above code prints all the characters in the string name one by one!

</p>