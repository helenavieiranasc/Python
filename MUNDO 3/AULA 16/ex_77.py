'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, 
para cada palavra, quais são as suas vogais.'''

tupla = ('helena', 'python', 'curso', 'mundo 3')

vogais = "aeiou"

for i in tupla:
    print(f"\nNa palavra {i} temos ", end="")
    for letra in i:
        if letra in 'aeiou':
            print(letra, end=' ')