'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o 
salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o 
empréstimo será negado.'''

print("-------- APROVADOR DE EMPRESTIMO -------")
valor_casa = float(input("Digite o valor da casa que vc deseja comprar: "))
salario = float(input("Digite o valor do seu salário: "))
anos = int(input("Digite em quantos anos vc gostaria de pagar: "))

parcela_mensal = valor_casa/(anos*12)
if parcela_mensal > (salario*0.3):
    print(f"Emprestimo negado! O valor da parcela é de {parcela_mensal:.2f} excede 30% de seu salario")
else:
    print(f"Vc devera pagar R${parcela_mensal:.2f}")