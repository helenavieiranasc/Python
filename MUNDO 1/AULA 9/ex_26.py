'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela 
aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input("digite uma frase: ")).lower().strip()
print(f'a letra A aparece {(frase.count("a"))} vezes')
print(f'a primeira letra A apareceu na posição {(frase.find("a") + 1)}')
print(f'a ultima letra A aparece na posição {(frase.rfind("a") + 1)}')