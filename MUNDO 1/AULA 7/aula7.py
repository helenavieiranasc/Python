print('-'*23)
print(' operações aritmeticas ')
print('-'*23)

print(pow(2,3)) # função interna de potencia (perde a ordem de precedencia)

print(144**0.5) # elevar a 1/2 gera a raiz quadrada do numero

print(pow(144, 0.5))

print(8**(1/3)) # elevar a 1/3 gera a raiz cubica do numero

nome = input('digite seu nome: ')
print(f'prazer em te conhecer {nome:20}!') # ":numero" da o tanto de espaços depois do valor digitado

nome = input('digite seu nome: ')
print(f'prazer em te conhecer {nome:>20}!') # ">" alinha os espaços p/ a direita

nome = input('digite seu nome: ')
print(f'prazer em te conhecer {nome:^20}!') # "^" centraliza o valor

nome = input('digite seu nome: ')
print(f'prazer em te conhecer {nome:-^20}!') # "'simbolo'^" centraliza o valor com o simbolo add

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
print(f'a soma entre {n1} e {n2} é igual a {n1 + n2}')