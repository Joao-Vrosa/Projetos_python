
from functools import reduce

def soma(x, y):
    return x + y

lista = [1, 2, 3, 4, 10, 20]

soma = reduce(soma,lista)

print(soma)

