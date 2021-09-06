def func():
    x = 50
    return x
x = 25

print(x)
print(func())
print(x)

o = 'oi'

def fofo():
    o = 'opa'

    def fofofo():
        print('hello', o)
    fofofo()

fofo()

y = 50

def foc():
    global y
    print('atual y ', y)
    y=25
    print('novo y ',y)

foc()
print(y) ## y global alterado


