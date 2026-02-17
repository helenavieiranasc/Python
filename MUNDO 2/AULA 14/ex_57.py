'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a 
digitação novamente até ter um valor correto.'''

sexo = input("digite seu sexo (m / f): ").lower()
while sexo != "m" and sexo != "f":
    print("resposta inválida!")
    sexo = input("digite seu sexo (m / f): ").lower()
if sexo == "f":
    print("arrasou!")
else:
    print("ok")