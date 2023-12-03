<h1>Python while Loop</h1>

As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

<h3>Example:</h3>

```python
count = 5
while (count > 0):
  print(count)
  count = count - 1
```

<h3>Output:</h3>
5 <br>
4 <br>
3 <br>
2 <br>
1

<br>

Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.

<h3>Else with While Loop :</h3>

We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

<h3>Example:</h3>

```python
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
```


<h3>Output:</h3>

5 <br>
4 <br>
3 <br>
2 <br>
1 <br>
counter is 0

<br>

<h1>Do-While loop in python</h1>

do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

<h3>Example</h3>

```python
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
```

<h3>Output</h3>

Enter a positive number: 1 <br>
1 <br>
Enter a positive number: 4 <br>
4 <br>
Enter a positive number: -1 <br>
-1

<br>

<h3>Explanation-</h3>

This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.