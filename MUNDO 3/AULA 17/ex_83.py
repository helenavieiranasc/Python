'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar 
se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expressão = input("digite a expressão: ")
pilha = []
for simbolo in expressão:
    if simbolo == '(':
      pilha.append("(")
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
    else:
        pilha.append(")")
        break

if len(pilha) == 0:
    print("ta valida!")
else:
    print("nn ta valida!")
