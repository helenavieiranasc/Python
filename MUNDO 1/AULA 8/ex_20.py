'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa 
que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import choice

a1 = input('digite seu nome: ')
a2 = input('digite seu nome: ')
a3 = input('digite seu nome: ')
a4 = input('digite seu nome: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista) # escolhe um aleatorio da lista
print(f'o aluno escolhido foi {escolhido}!')


a1 = input('digite seu nome: ')
a2 = input('digite seu nome: ')
a3 = input('digite seu nome: ')
a4 = input('digite seu nome: ')
lista = [a1, a2, a3, a4]
ordem = sorted(lista) # não faz uma ordem aleatória
print(f'a ordem de apresentação do trabalho será \n{ordem}')