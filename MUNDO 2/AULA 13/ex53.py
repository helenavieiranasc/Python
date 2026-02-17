'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = input("Digite sua frase: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for i in range(len(junto) -1, -1, -1):
    inverso += junto[i]
print(f"{junto} o inverso é {inverso}")
if inverso == junto:
    print("Temos um palindromo!")
else:
    print("Não temos um palindromo!")
