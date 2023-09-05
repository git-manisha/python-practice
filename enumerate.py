l1 = ["eat","sleep","repeat"]
s1 = "manisha"

obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:",type(obj1))
print(list(enumerate(l1)))

print(list(enumerate(s1,2)))
print()

for ele in enumerate(l1):
    print(ele)

for count,ele in enumerate(l1,100):
    print(count,ele,end=" ")
print()

for count , ele in enumerate(l1):
    print(count)
    print(ele)




