'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos 
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

dias = int(input('digite por quantos dias vc alugou o carro: '))
km_rodado = float(input('digite quantos km foram rodados: '))
valor = (60*dias) + (0.15*km_rodado)
print(f'vc devera pagar R${valor:.2f}')