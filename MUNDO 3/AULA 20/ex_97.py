'''Faça um programa que tenha uma função chamada escreva(), que receba um 
texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(txt):
    palavra = txt
    print("~" * len(palavra))
    print(txt)
    print("~" * len(palavra))


escreva("Helena")
escreva("Curso em vídeo - Python")
escreva("Exercício 97")