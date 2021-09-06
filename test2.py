st = 'Print only the words starting with s in this sentence'
print(st)
x = st.split()
print(x)

for i in x:
    if i[0] == 's':
        print(i)
    else:
        continue

x = [i for i in range(0, 11) if i % 2 == 0]
print(x)

j = [i for i in range(0, 51) if i % 3 == 0]
print(j)

st = 'Print every word in this sentence that has an even number of letters'
x = st.split()

for i in x:
    if len(i) % 2 == 0:
        print(i, 'par')
    else:
        continue

for i in range(0,101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    else:
        if i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

st = 'Create a list of the first letters of every word in this string'
x = st.split()
b = []
for i in x:
    b += [i[0]]
print(b)

c = [i[0] for i in st.split()]
print(c)

