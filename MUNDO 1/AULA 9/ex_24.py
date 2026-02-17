'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''

nome = input("digite o nome da cidade: ").lower().strip()
if "santo" in nome:
    print("Santo está no nome da cidade")
else:
    print("Santo não esta no nome da cidade")


nome = input("digite o nome da cidade: ").lower().strip()
print("santo" in nome)


# pra saber se COMEÇA com Santo
cidade = str(input('digite o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == "SANTO")