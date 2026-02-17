''' Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

# com variavel
numero = int(input('digite um numero: '))
antecessor = numero - 1
sucessor = numero + 1
print(f'o antecessor de {numero} é {antecessor} e seu sucessor é {sucessor}')

# sem variavel
numero = int(input('digite um numero: '))
print(f'o antecessor de {numero} é {numero - 1} e seu sucessor é {numero + 1}')