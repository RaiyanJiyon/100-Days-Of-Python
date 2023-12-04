<h1>Python Functions</h1>

<p> function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.</p>

There are two types of functions:

<ol>
<li>Built-in functions</li>
<li>User-defined functions</li>
</ol>

<h3>Built-in functions:</h3>

These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

<strong>min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(),</strong> etc.

<h3>User-defined functions:</h3>

We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

<h3>Syntax:</h3>

```python
def function_name(parameters):
  pass
  # Code and Statements
```

<ul>
<li>Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).</li>
<li>Any parameters and arguments should be placed within the parentheses.</li>
<li>Rules to naming function are similar to that of naming variables.</li>
<li>Any statements and other code within the function should be indented.</li>
</ul>




<h3>Calling a function:</h3>
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

<h3>Example:</h3>

```python
def name(fname, lname):
    print("Hello,", fname, lname)
name("Sam", "Wilson")

```

<h3>Output:</h3>

Hello, Sam Wilson