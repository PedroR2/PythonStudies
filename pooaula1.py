import math
l = [1, 2, 3]
print(type(l))

def funcao(a, b):
    return a+b

print(type(funcao))

class Sample(object):
    pass

x= Sample()

print(type(x))

class Dog(object):
    especie = 'mamifero'
    def __init__(self, raca, altura):
        self.raca = raca
        self.altura = altura
    def latir(self):
        print('auau')

sam = Dog(raca= 'labrador', altura= 1.62)
sam = Dog('labrador', 1.62)

print(sam.raca)
print(sam.altura)
print(sam.especie)
sam.latir()

class circulo(object):
    pi= 3.14
    def __init__(self, raio= 1):
        self.raio = raio
    def area(self):
        return self.pi*(self.raio**2)
    def defraio(self, raio):
        self.raio = raio
    def obtraio(self):
        return self.raio


c = circulo()
c = circulo(3)
print(c.obtraio())
print(c.area())
c.defraio(4)
print(c.obtraio())

class Animal(object):
    def __init__(self):
        print('animal criado.')
    def quemsou(self):
        print('eu sou um animal')
    def comer(self):
        print('comendo')

animal1 = Animal()

animal1.quemsou()

class cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('cachorro criado')
    def quemsou(self):
        print('cachorro')
    def latir(self):
        print('auau')

sam = cachorro()
sam.quemsou()
sam.latir()
sam.comer()

class book(object):
    def __init__(self, titulo, autor, paginas):
        print('livro criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def __str__(self):
        return 'titulo: {a}'.format(a= self.titulo) + '\nautor: {b}'.format(b= self.autor) + '\npaginas: {c}'.format(c= self.paginas)
    def __len__(self):
        return self.paginas
    def __del__(self):
        print('livro destruido')


livro1 = book('uma vez', 'pedro', 164)

print(livro1)
print(len(livro1))
print(livro1.autor)
print(livro1.paginas)
del livro1

#trabalho

class Line(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def comprim(self):
        return ((((self.arg2[1]-self.arg1[1])**2)+((self.arg2[0]-self.arg1[0])**2))**(0.5))
    def ang(self):
        print(Line.comprim(self))
        return math.asin((self.arg2[1]-self.arg1[1])/Line.comprim(self))



a = Line((3,2),(8,10))
print(a.comprim())
print(a.ang())





