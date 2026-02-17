'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que 
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('digite a velocidade do seu carro (km/h): '))

if velocidade > 80:
    multa = (velocidade - 80)* 7 
    print(f'Você passou dda velocidade limite e tem uma multa no valor de R${multa:.2f}')
else:
    print('Você não ultrapassou a velocidade limite!')