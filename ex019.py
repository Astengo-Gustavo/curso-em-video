'''
um professor quer sortear um dos seus quatro aluno
para apagar o wusfro.faça um programa que ajude ele, lendo
o nome deles e escrevendo o nome escolhido
'''
from random import choice
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('ultimo aluno: ')
lista = [n1, n2, n3, n4]

sorteio = choice(lista)

print('o aluno escolhido foi {}'.format(sorteio))