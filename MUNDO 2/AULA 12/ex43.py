'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e 
mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

peso = float(input("digite seu peso (kg): "))
altura = float(input("digite sua altura (m):"))

imc = peso / (altura**2)
print(f"seu imc é de {imc:.1f}")

if imc < 18.5:
    print("vc ta abaixo do peso")
elif 18.5 < imc < 25:
    print("vc ta no peso ideal")
elif 25 < imc < 30:
    print("vc ta c sobrepeso")
elif 30 < imc < 40:
    print("vc ta c obesidade")
else:
    print("vc ta c obesidade morbida")