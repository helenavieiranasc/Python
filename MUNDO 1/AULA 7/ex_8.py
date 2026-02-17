'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

valor_metros = int(input('digite um valor em metros: '))
valor_cm = valor_metros*100
print(f'{valor_metros} metros em cm é {valor_cm}')
valor_mm = valor_metros*1000
print(f'{valor_metros} metros em mm é {valor_mm}')


valor_m = int(input('digite um valor em metros: '))
print(f'a medida de {valor_m}m corresponde a: ')
print(f'{valor_m/1000}km')
print(f'{valor_m/100}hm')
print(f'{valor_m/10}dam')
print(f'{valor_m*10}dm')
print(f'{valor_m*100}cm')
print(f'{valor_m*1000}mm')
