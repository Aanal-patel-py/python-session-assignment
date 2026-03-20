
def mydecorator(func):
    def sum(a,b):
        func(a,b)
        x= a+b
        print("sum"+ str(x))
        return x
    return sum



@mydecorator
def func(a,b):
    print(a)

    print(b)



func(2,3)


