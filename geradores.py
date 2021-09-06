## nao sao precarregados na memoria de uma vez so

def gen_cubes(n):
    for num in range(n):
        yield num ** 3 ## yield != return, yield cria e outputa imediatamenet nao mantem a lista na memoria. pode usar o valor que for
                       ## e nao tem risco de travar o pc pq n acumula tudo na memoria.

l = []
a = 3 ** 4
l.append(a)


def gen_cubes2(n): #cria previamente a lista inteira na memoria
    l = []

    for num in range(n):
        l.append(num ** 3)
    return l



for x in gen_cubes(10):
    print(x)

for a in gen_cubes2(10):
    print(a)


def fibbo(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for i in fibbo(10):
    print(i)
print(list(fibbo(10)))


g = fibbo(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


s = 'hello'
print(list(s))
s_it = iter(s)
print(next(s_it))
print(next(s_it))
print(next(s_it))