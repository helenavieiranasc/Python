'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preco = float(input('digite o valor do produto: '))
desconto = preco - preco*0.05
print(f'o produto com desconto de 5% fica no valor de R${desconto:.2f}')