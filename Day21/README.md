<h1>Function Arguments and Return Statement</h1>

<p>There are four types of arguments that we can provide in a function:</p>

<ul>
<li>Default Arguments</li>
<li>Keyword Arguments</li>
<li>Variable length Arguments</li>
<li>Required Arguments</li>
</ul>

<h3>Default Arguments:</h3>
<p>We can provide a default valuewhile creating a function. This waythe function assumes a default valueeven if a value is not provided in thefunction call for that argument.</p>

```python
def name(fname, mname="Jhon", lname="Whatson"):
    print("Hello,", fname, mname, lname)
name("Amy")
```



<h3>Output:</h3>
   
Hello, Amy Jhon Whatson


<h3>Keyword Arguments:</h3>
<p>We can provide arguments with key = value; this way, theinterpreter recognizes the arguments by the parameter name.The order in which the arguments are passed does not matter.<p>

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname="Peter", lname="Wesker", fname="Jade")
```


<h3>Output:</h3>

Hello, Jade Peter Wesker


<h3>Required Arguments:</h3>

<p>In case we don’t pass the arguments with a key = valuesyntax, then it is necessary to pass the arguments in thecorrect positional order, and the number of arguments passedshould match the actual function definition.</p>

<p>Example 1: when the number of arguments passed does not match the actual function definition.</p>

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Quill")
```

<h3>Output:</h3>

TypeError: name() missing 1 required positional argument: 'lname'

<h3>Example 2: when the number of arguments passed matches the actual function definition.</h3>

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")
```

<h3>Output:</h3>

Hello, Peter Ego Quill


<h3>Variable-length Arguments:</h3>

<p>Sometimes we may need to pass more arguments than thosedefined in the actual function. This can be done usingvariable-length arguments.</p>

<p>There are two ways to achieve this:</p>

<h3>Arbitrary Arguments:</h3>
<p>While creating a function, pass a * before the parametername while defining the function. The function accesses thearguments by processing them in the form of a tuple.</p>

```python
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")
```

<h3>Output:</h3>

Hello, James Buchanan Barnes


<h4>Keyword Arbitrary Arguments:</h4>
<p>While creating a function, pass a * before the parametername while defining the function. The function accesses thearguments by processing them in the form of a dictionary.</p>

```python
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname="Buchanan", lname="Barnes", fname="James")
```

<h3>Output:</h3>

Hello, James Buchanan Barnes


<h3>Return Statement:</h3>
<p>The return statement is used to return the value of the expression back to the calling function.</p>

```python
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))
```

<h3>Output:</h3>

Hello, James Buchanan Barnes

