print("manisha")
c='a'
print(type(c))
print(int(123.33))
print(int(True))
print(int('10'))
print(float(10))
print(float("10.20"))
print(complex(10))
print(complex(10.5))
print(complex(True))
print(complex(False))
print(complex("10"))
print(complex(10,20))
print(complex(10,-2))
print(bool(0))
print(bool(True))
print(str(10))
print(str("manisha"))
print(str(10+5j))
print(str(True))
print()

a=10
b=10
print(a is b)
print(id(a))
print(id(b))
a=20
print(id(a))
print(id(b))

x=10+5j
y=10+5j
print(id(x))
print(id(y))
print(x is y)
print()

x = [10,20,30,40]
print(x)
print(type(x))
b = bytes(x)
print(type(b))
print(b[0])
print(b[1])

print(b)
for i in b:
    print(i)

print()
s = bytearray(x)
s[0] = 40
for i in s:
    print(i)

list=[10,10.2,'manisha',True,10]
print(list)
for i in list:
    print(i,end="-")
print()

l=[10,20,30,40]
print(l[0])
print(l[-1])
print(l[1:3])
l[0]=100
print(l)
for i in l:
    print(i)

l.append("durga")
print(l)
l.remove(30)
print(l)
l1=l*3
print(l1)
t=(10,20,30,40,10,"manisha")
print(type(t))
print(t)
print()

print(range(10))
for i in range(10,20,2):
    print(i)

r=range(10,20)
print(r[0])
s={100,10,0,"manisha"}
print(s)
s.add(60)
print(s)
s.remove("manisha")
print(s)
s.add(70)
print(s)
s1={10,20,30,"10"}
print(type(s1))
fs=frozenset(s1)
print(type(fs))
print(fs)
for i in fs:
    print(i)

print()
d={101:'durga',102:'manisha',103:'muskan'}
print(d)
d[101]="vikas"
print(d)

d1={}
d1['a']='apple'
d1['b']='banana'
d1['c']='cat'
print(d1)
print()

s="durga\nsoftware"
print(s)
s="durga\tsoftware"
print(s)
s="This is \" symbol"
print(s)
s="durga\\software"
print(s)