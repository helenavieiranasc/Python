dados = {"nome": "Pedro", "idade": "25"}

print(dados)

print(dados["nome"])
print(dados["idade"])

dados["sexo"] = "M"
print(dados["sexo"])

del dados["idade"]
print(dados)

filme ={"título": "star wars", "ano": "1977", "diretor": "George Lucas"}

print(filme.values()) # retorna os valores adicionados a cada categoria
print(filme.keys()) # retorna as chaves (nomes das "categorias")
print(filme.items()) # retorna as chaves e seus valores

for k, v in filme.items():
    print(f"O {k} é {v}")

estado = {}
brasil = []

for i in range(0, 3):
    estado["UF"] = input("Unidade federativa: ")
    estado["SIGLA"] = input("Sigla: ")
    brasil.append(estado.copy()) # dicionario adicionado a uma lista
for e in brasil:
    for k, v in estado.items():
        print(f"{k} = {v}")
