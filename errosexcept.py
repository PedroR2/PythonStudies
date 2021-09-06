try:
    a = open('texto.txt','w')
    a.write('eae galera')
except IOError:
    print('nao achei o arquivo')
else:
    print('impresso com sucesso')
finally:
    print('isso sempre vai ser executado')

for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except:
        print('deu nao')

def quadr():
    a = 0
    while a < 1:
        try:
            print('digite um valor: ')
            arg1 = int(input())
            b = arg1**2
            if b >= 0:
                print('o quadrado e: ', b)
                a += 1
        except:
            print('valor invalido tente dnv')

def quadr2():
    while True:
        print('digite um valor: ')
        try:
            arg1 = int(input())
            b = arg1**2
            print(b)
            break
        except:
            print('valor invalido tente dnv')
            continue

quadr2()

