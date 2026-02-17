'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

numero = int(input("digite um numero: "))

fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1
print(f"O fatorial é {fatorial}")