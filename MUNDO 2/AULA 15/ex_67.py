'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O 
programa será interrompido quando o número solicitado for negativo.'''

while True:
    n = int(input("digite um numero: "))
    if n < 0:
        break
    else:
        for i in range(1, 11):
            print(f"{i} x {n} = {i * n}")
        continuar = input("s/n: ").lower()
        if continuar == "s":
            continue
        else:
            break