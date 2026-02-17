'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario = float(input('digite seu salario: '))
aumento = salario + salario*0.15
print(f'seu salario com aumento fica R${aumento:.2f}')