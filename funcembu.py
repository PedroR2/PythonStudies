def fahre(temp):
    return (9/5) * (temp + 32)

print(fahre(2))

temp = [1,2,3,4,5]

for i in temp:
    print("%.2f" %(fahre(i)))

c = 'oi galera do mal'
print(c.split())
print(list(map(len, c.split())))

print(list(map(fahre, temp)))
print(list(map(lambda temp: (9 / 5) * (temp + 32), temp))) #lambda n grava na memoria

l = [1,2,3,4]


##reduce(lambda a, b: a + b, l)


print(list(filter(lambda a: a%2 == 0, l)))

a = [1,2,3]
b = [4,5,6]
c = zip(a,b)

for i in c:
    print(max(i))

c = zip(a,b)
print(list(c))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

print(list(zip(d1, d2.values())))

o = ['a', 'b', 'c', 'd', 'e']

for number, item in enumerate(o):
    print(number, '-', item)

g = [True, True, True, False, True]

print(all(g)) #tudo vdd
print(any(g)) #algum vdd



