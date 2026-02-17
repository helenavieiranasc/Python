'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu 
programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input("digite um número de 0 a 20: "))
    if numero < 0 or numero > 20:
        print("Por favor digite numeros apenas de 0 a 20, tenta de novo!")
    else:
        print(f"vc digitou o número {tupla[numero]}")
        break