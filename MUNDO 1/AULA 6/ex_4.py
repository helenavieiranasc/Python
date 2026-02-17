'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

variavel = (input("digite algo: "))
print(f'o tipo da variavel é: {(type(variavel))}')
print(f'é um numero? {variavel.isnumeric()}')
print(f'é uma letra? {variavel.isalpha()}')
print(f'é alfabetico numerico? {variavel.isalnum()}')
print(f'são letras maisculas? {variavel.isupper()}')
print(f'são letras minusculas? {variavel.islower()}')
print(f'só tem espaços? {variavel.isspace()}') # diz se só tem espaço
print(f'esta capitalizada? {variavel.istitle()}') # diz se esta capitalizada (maiusculas e minusculas)