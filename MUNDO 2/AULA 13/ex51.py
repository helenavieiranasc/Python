'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos 
dessa progressão.'''

pt = int(input("Digite o primeiro termo da pa: "))
razao = int(input("digite a razao da pa: "))
for i in range(1, 11):
   i = pt + (i - 1)*razao
   print(i)
