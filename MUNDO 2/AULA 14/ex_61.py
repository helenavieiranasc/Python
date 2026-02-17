'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

pt = int(input("Digite o primeiro termo da pa: "))
razao = int(input("digite a razao da pa: "))
c = 0
while c < 10:
   termo = pt + (c - 1)*razao
   print(termo)
   c += 1
