'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.'''

info = []
dados = []
leves = []
pesado = []

while True:
    nome = dados.append(input("Digite seu nome: "))
    peso = dados.append(float(input("Digite seu peso: ")))
    if dados[1] < 70:
        leves.append(dados[0])
    else:
        if dados[1] > 100:
            pesado.append(dados[0])
            
    info.append(dados[:])
    dados.clear()
    
    continuar = input("Quer continuar (s/n):").strip().lower()
    if continuar == "s":
        continue
    else:
        print(f"Foram cadastradas {len(info)} pessoas")
        if len(pesado) == 0:
            print("Não foram cadastradas pessoas pesadas! (mais de 100kg) ")
        else:
            print(f"Os maiores pesos foram de {pesado}")
        
        if len(leves) == 0:
            print("Não foram cadastradas pessoas leves! (menos de 70kg) ")
        else:
            print(f"Os menores pesos foram de {leves}")

        break

