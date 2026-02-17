'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

reais = float(input('quantos reais você tem? R$'))
dolares = reais/3.27
print(f'com R${reais} você consegue comprar ${dolares:.2f}')