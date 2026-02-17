'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários 
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('digite seu salario: '))

if salario >= 1250:
    novo_salario = salario + (salario*0.10)
else:
    novo_salario = salario + (salario*0.15)
print(f'seu novo salario sera de R${novo_salario}')