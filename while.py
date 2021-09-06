x = 0
y = 0
while x < 10 or y < 20:
    if x < 10 and y < 20:
        print('x ainda e menor que dez', x)
        print('y ainda e menor que vinte', y)
        y += 1
        x += 1
    if x >= 10 and y < 20:
        print('x ja e dez', x)
        print('y ainda nao e 20', y)
        y += 1
else:
    print('x e igual a dez', x)
    print('y e igual a vinte', y)


x = 1
liss = []

while True:
    liss += [x]
    x += 1
    print(liss)
    if x > 10:
        break ## encerra o loop
liss[1] = 'a'
print(liss)

x = 0

while x < 50:
    x += 1
    if x % 2 == 1:
        continue  ## para nesse ponto e recomeca o loop
    if x % 2 == 0:
        print('e par', x)

