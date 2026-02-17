lista = ["lanche", "suco", "pizza", "sorvete"]

lista_vazia = []
lista_vazia2 = list()

################ INSERIR EM UMA LISTA ######################

lista.append("cookie")
print(lista)

lista.insert(0, "cachorro quente") # add em um lugar específico da lista
print(lista)

########## REMOVER DE UMA LISTA ##############################

del lista[3] # deleta o item
print(lista)

lista.pop(4) # geralmente deleta o ultimo item mas tbm pode passar parametro
print(lista)

lista.remove("sorvete") # remove pelo conteudo (remove o primeiro q aparecer no caso de ter mais de um elemento igual)
print(lista)

if "suco" in lista:
    lista.remove("suco")
else:
    lista.append("agua")
print(lista)


###############################################################

valores = list(range(4, 11))
print(valores)

valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)

valores.sort() # organiza em ordem
print(valores)

valores.sort(reverse = True) # organiza em ordem contraria
print(valores)

print(len(valores))

################################################################

for v in valores:
    print(f"{v}...", end='')
    print(v)

a = [2, 3, 4, 7]
b = a
b[2] = 8 # muda as duas pq a partir do memento q eu igualo cria um ligação entre elas
print(f"lista a: {a}")
print(f"lista b: {b}")

c = [2, 3, 4, 7]
d = c [:] # d recebe uma cópia de todos os elementos de c
d[2] = 8 
print(f"lista c: {c}")
print(f"lista d: {d}")