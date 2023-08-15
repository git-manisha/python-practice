def f1():
    def inner(a,b):
        print("The Sum:",a+b)
        print("The Average:",(a+b)/2)
    inner(10,20)
    inner(20,30)
    inner(40,50)
f1()
print()

#a function can return another function
def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    print("outer function returning inner function")
    return inner
f2=outer()
f2()
print()

#function Decorators
def decor(func):
    def inner(name):
        if name=="Sunny":
            print("hello Sunny bad morning")
        else:
            func(name)
    return inner

#@decor
def wish(name):
    print("hello",name,"Good morning")

wish("durga")
wish("Ravi")
wish("Sunny")


#without decorator
def decor(func):
    def inner(name):
        if name=="Sunny":
            print("hello Sunny bad morning")
        else:
            func(name)
    return inner


#@decor
def wish(name):
    print("hello",name,"Good morning")
decorfunction=decor(wish)

wish("durga")
wish("Ravi")
wish("Sunny")
decorfunction("Sunny")
print()

#another decorator program
def smartdivision(func):
    def inner(a,b):
        if b==0:
            print("hello Stupid...how we can divide with zero")
        else:
            return func(a,b)
    return inner
@smartdivision
def division(a,b):
    return a/b
print(division(12,2))
print(division(10,5))
print(division(10,0))