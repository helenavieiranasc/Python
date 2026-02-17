# analise -> analisa strings
frase = "hello world"
print(len(frase)) # len -> vem de length me da o comprimento da frase (qtd. de caracteres)

frase = "hello world"
print(frase.count("o")) # count -> conta a qtd. de caracteres especificos na string

frase = "hello world"
print(frase.count("o", 0, 5)) # vai contar apenas de onde foi especificado

frase = "hello world"
print(frase.find("llo"))  # me indica a posição onde começa a parte da string que quero encontrar

frase = "hello world"
print(frase.find("a")) # quando não é encontrado a string, retorna -1

frase = "hello world"
print("hello" in frase)

frase = "hello world"
print("oii" in frase)

# divisão
frase = "hello world"
print(frase.split()) # separa cada palavra de frase em uma string e são colocadas dentro de uma lista

# fatiamento -> pega apenas o caracter desejado da string
frase = "hello world"
print(frase[4])

frase = "hello world"
print(frase[4:9])

frase = "hello world"
print(frase[0:11:2]) # start:stop:step onde começa, onde para e quanto vai saltar

frase = "hello world"
print(frase[:4])  # quando nao especifica onde começa, começa do zero

frase = "hello world"
print(frase[4:])  # quando nao especifica onde termina, vai até o final

frase = "hello world"
print(frase[4::3]) 

# junção
frase = ["hello", "world"]
print(" ".join(frase)) # junta strings de uma lista com separador especifico

# transformação 
frase = "hello world"
print(frase.replace('hello', 'oii')) # troca uma parte por outra

frase = "hello world"
print(frase.upper())  # transforma os caracteres todos para maiusculo

frase = "HELLO WORLD"
print(frase.lower())  # transforma os caracteres todos para minusculo

frase = "hello world"
print(frase.capitalize()) # transforma tudo em minusculo menos a primeira letra

frase = "hello world"
print(frase.title()) # transforma tudo em minusculo menos a primeira letra - de cada palavra -

frase = "  hello world  "
print(frase.strip()) # remove os caracteres com espaços antes e depois da frase

frase = "  hello world  "
print(frase.rstrip()) # remove os caracteres com espaços a direita (r -> rigth)

frase = "  hello world  "
print(frase.lstrip()) # remove os caracteres com espaços a esquerda (l -> left)