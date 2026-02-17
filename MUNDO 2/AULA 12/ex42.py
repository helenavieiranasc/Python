'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

lado_1 = float(input('digite o primeiro lado: '))
lado_2 = float(input('digite o segundo lado: '))
lado_3 = float(input('digite o terceiro lado: '))

if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
    print('esses lados podem formar um triangulo!')
    
    if lado_1 == lado_2 == lado_3:
        print("é do tipo equilatero")
    elif lado_1 != lado_2 != lado_3 != lado_1:
        print("é escaleno")
    else:
        print("é isoceles")
else:
    print('esses lados não podem formar um triangulo!')
