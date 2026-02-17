'''Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []

for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}],[{c}]: "))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
        else:
            continue

print("-"*40)

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()

print(f"\nTodos os valores pares da matriz somados resultam em {sum(pares)}")
print(f"Os valores da 3º coluna somados resultam em {(matriz[0][2] + matriz[1][2] + matriz[2][2])}")
print(f"O maior valor da 2º linha é {max(matriz[1])}")