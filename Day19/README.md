<h1>break statement-</h1>

<p>The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.</p>

<h3>example-</h3>

```python
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")
```


<h3>output:</h3>

1 Mississippi <br>
2 Mississippi <br>
3 Mississippi <br>
4 Mississippi <br>
5 Mississippi <br>
. <br>
. <br>
. <br>
50 Mississippi <br>




<h1>Continue Statement-</h1>

The continue statement skips the rest of the loop statements and causes the next iteration to occur.

<h3>example-</h3>

```python
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

```

<h3>output:</h3>

2 <br>
4 <br>
6 <br>
8 <br>
0 