# ceil -> arredonda pra cima
# floor -> arredonda pra baixo
# trunc -> elimina da virgula pra frente
# factorial -> calcula fatorial

import math
n = int(input('digite um numero: '))
raiz = math.sqrt(n)
print(raiz) 

from math import sqrt  # importa só a função sqrt
n = int(input('digite um numero: '))
raiz = sqrt(n)  # nao precisa do "math." na frente
print(raiz) 

import math
n = int(input('digite um numero: '))
raiz = sqrt(n)
print(math.trunc(raiz)) 

import math
n = int(input('digite um numero: '))
raiz = math.sqrt(n)
print(math.ceil(raiz))

import math
n = int(input('digite um numero: '))
raiz = math.sqrt(n)
print(math.floor(raiz)) 