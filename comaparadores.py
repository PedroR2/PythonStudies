a = 3
b = 2
c = 4

print((b == c or b == 4) and b == 3)

if a > b:
    a = 2
    b = 4
elif c > a:
    a = 5
    b = 6
else:
    a = 8
    b = 10

print(type(a))
print('a= %1.2f \n b= %1.2f' %(a,b))

b = {'eu': 9, 'ela': 4}
j = 'ela'
if b[j] >= 7:
    print('aprovado')
else:
    print('reprovado')

p = ['a','b','c','oi',1,2,3]
d = [1,2,3,4,5,6,7,8,9,10]
for el in d:
    if el%2 == 0:
        print(el, 'par')
    elif el%2 == 1:
        print(el, 'impar')

soma = 0

for el in d:
    soma += el
print('somatorio =', soma)

m = 'oi gente'

for el in m:
    print(el)



print('\n')
print('%1.2f' %(22%56)) ## resto da divisao

n = [(1,2), (3,4), (5,6)]

(t1,t2) = n[0]
print(t1,t2)

for (el1,el2) in n:
    print(el1,el2)

b = {'ch1': 1, 'ch2': 2, 'ch3': 3}

print(b.items())

for ch in b.items():
    print(ch)

for ch,val in b.items():
    print(ch,val)

for ch in b:
    print('chave', ch)
    print('valor', b[ch])


$django-admin startproject mysite