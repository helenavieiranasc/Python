'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
– A média da turma
- A situação (opcional)'''

def notas(*num, sit=False):
    """
    Docstring for notas
    -> Função para analisar notas e situação de vários alunos
    :param num: Quantidade de notas (aceita várias)
    :param sit: (Opcional) Mostra a situação
    :retorno: Dicionário com várias informações sobre a turma
    """
    infos = {"total": (len(num)), "maior nota": (max(num)), "menor nota": (min(num)), "media": (sum(num))/len(num)}
    if sit == True:
        if infos["media"] >= 7:
            infos["situação"] = "BOA!"
        else:
            infos["situação"] = "RUIM!"
    return infos

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)