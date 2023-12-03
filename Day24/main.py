#Python Tuples

tup = (10,20,50,33)

print(type(tup))
print(tup)

print(tup[:])

tup2 = tup[2:3]
print(tup2)

tup3 = (1)
print(type(tup3)) #because python confused 1 is in tupple or not

tup3 = (1,)
print(type(tup3)) #so we will use , at the end of elements


if 10 in tup:
    print("Yes")
else:
    print("NO")