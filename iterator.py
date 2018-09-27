"""
Iterable,iteration, iterator
s="Python"
for i in s:
    print(i)
Iterable:s=>iter()
iteration: for loop
iterator: i=>next()

s=set("1,2,3,4,5,6")
it=iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(it[0])

#Generators:
def demo(a,b):
    yield a+b
    yield a*b, a+b
a=demo(9,6)
print(next(a))
print(next(a))
print(next(a))

list(map(function, iterables))
list(filter(function, iterable))

import functools
functools.reduce(function, iterable)
1,2,3,4,5,6,7,8,9,10

"""


















