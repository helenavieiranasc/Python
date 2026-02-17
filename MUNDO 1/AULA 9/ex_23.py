'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

# convertendo para string
numero = int(input("digite um numero de 0 a 9999: "))
n = str(numero)
print(f'unidade: {(n[3])}')
print(f'dezena: {(n[2])}')
print(f'centena: {(n[1])}')
print(f'milhar: {(n[0])}')


# matematica
numero = int(input('digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10 
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')