a=10
b=2
print(a)
print("a+b=",a+b)
print("a-b=",b-a)
print("a*b=",a*b)
print("a/b=",b/a)
print("a//b=",a//b)
print("a%b=",a%b)
print("a**b=",a**b)
print()
print("manisha"+"soni")
print("durga"+"10")
print("lovely"*3)
print(4*"soni")

#RelationOperator
a=10
b=20
print("a>b is",a>b)
print("a>=b is",a>=b)
print("a<b is",a<b)
if(a>b):
    print("a is greater than b")
else:
    print("a is not greater than b")

x="manisha"
y="soni"
print(x>=y)
print(2<True)
print(10<20<30<5) #chaining
print(10!=20)

#LogicalOperators
print(True and False)
print(True or False)
print(not False)
print(10 and 20)
print(20 and 0)
print()

print(4&5)
print(True & True)
print(4|5)
print(4^5)
print(~1)
print(10<<2)
print(10>>2)
print()

a,b=10,20
x=30 if a>b else 40
print(x)

#ternary operator
'''a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
min = a if a<b and a<c else b if b<c else c
max = a if a>b and a>c else b if b>c else c
print("Minimum value:",min)
print("Maximun value:",max)'''
print()

#special operator
x=10
y=10
print(x is y)
print(x is not y)

a="durga"
b="durga"
print(id(a))
print(id(b))
print(a is b)

list1=['one','two','three']
list2=['one','two','three']
print(id(list1))
print(id(list2))
print(list1 is not list2)
print(list2 == list1)
print()

#membership operators
x="hello learning python is very easy"
print('h' in x)
print('easy' in x)
print('manisha' not in x)
print()

import math
print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
print(math.e)
print(math.nan)

import math as m
print(m.pow(3,3))
print(m.sqrt(81))

from math import sqrt,pi
print(sqrt(64))
print(pi)

from math import pi
r=4
print("Area of circle is:",pi*r**2)