def funk():
    return 1

print(funk())

s = 'global variavel'

def funk():
    a = 1
    print(locals())

funk()
print(globals()['s'])

def hello(nome = 'pedro'):
    return 'Ola ' + nome


print(hello())

boasv = hello

print(boasv())

def hello(nome = 'pedro'):
    print('Ola ' + nome)
    def tdb():
        print('tdb?')
    def cmv():
        print('cmvd?')
    if nome == 'pedro':
        return tdb()
    else:
        return cmv()
    print(locals())

hello('lucas')

def hello(nome = 'pedro'):
    print('Ola ' + nome)
    def tdb():
        print('tdb?')
    def cmv():
        print('cmvd?')
    if nome == 'pedro':
        return tdb
    else:
        return cmv
    print(locals())

f = hello('pedro')
f()

def novo_decorador(func):
    def func_interna():
        print('codigo antes da funcao')
        func()
        print('codigo dps da funcao')
    return func_interna

def precisa_decorar():
    print('precisa de decorador')

precisa_decorar = novo_decorador(precisa_decorar)
print(type(precisa_decorar))
precisa_decorar()

def novo_decorador2(func):
    def func_interna():
        print('codigo antesssss da funcao')
        func()
        print('codigo dps da funcao')
    return func_interna


@novo_decorador2
def precisa_decorar():
    print('precisa decorar')

precisa_decorar()
