'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de 
tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

largura = float(input('digite a largura da parede: '))
altura = float(input('digite a altura da parede: '))
area = largura*altura
litro_tinta = area/2
print(f'a area da sua parede é de {area} metros quadrados, você precisa de {litro_tinta} litros de tinta para pinta-la')