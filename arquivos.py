import os

print(os.getcwd())

file = open('texto.txt', 'a')
file.seek(0)
escrever = ['linha 4', 'linha 5']
for linha in escrever:
    file.write(linha)
    file.write('\n')
file.close()

file = open('texto.txt')

file.seek(0)
print(file.read())


file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())



