from collections import Counter

l = [1, 2, 2, 2, 'a', 'a', 'b', 3, 4, 5]
print(Counter(l))
p = 'quantas palavras tem aqui aqui'
b = Counter(p.split())
print(Counter(p.split()))
print(b.most_common())

from collections import defaultdict

d = {}
d['one'] = 1
print(d)
d2 = defaultdict(object)
d2['one'] = 1
print(d2)
print(d2['two'])
print(d2)
d3 = defaultdict(lambda : 32) ## cria e preenche valores caso chame chaves que nao existem
print(d3['one'])
print(d3)

from collections import namedtuple

t = (1, 2, 3)
dog = namedtuple('dog', 'age breed name')
sam = dog(age = 2, breed= 'aviao', name= 'sam')

print(sam)
print(sam.age)
print(sam[0])

import datetime

t = datetime.time(4, 20, 1)
print(t)
print(t.hour)
print(t.minute)
print(t.tzinfo) ##timezone
print(t.min)
print(t.max)
print(t.resolution)
today = datetime.date(2014, 3, 2)
todayy = datetime.date.today()
print(today)
print(todayy)
print(todayy.ctime())
todayyy = datetime.datetime(2016, 11, 10, 4, 20, 3) #com tempo
print(todayyy.ctime())
todayyyy = datetime.date.today()
print(todayyyy.resolution)

to = todayyyy.strftime('%Y-%m-%d')
print(to)


