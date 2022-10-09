'''
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0,2)

pergunta = int(input(''' Escolha uma opção para se jogar:

[0] Pedra
[1] Papel
[2] Tesoura

Digite sua escolha: '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POH!!!')
sleep(1)
print('-='*20)
print('O computador escolheu: {}'.format(lista[computador]))
print('O jogador esoclheu: {}'.format(lista[pergunta]))
print('-='*20)
if computador == 0:
    if pergunta == 0:
        print('Empate!')
    elif pergunta == 1:
        print('Jogador venceu!')
    elif pergunta == 2:
        print('Computador venceu! ')
    else:
        print('Opção invalida')
elif computador == 1:
    if pergunta == 0:
        print('Computador venceu!')
    elif pergunta == 1:
        print('Empate!')
    elif pergunta == 2:
        print('Jogador venceu!')
    else:
        print('Opção invalida')
elif computador == 2:
    if pergunta == 0:
        print('Jogador venceu!')
    elif pergunta == 1:
        print('Computador venceu!')
    elif pergunta == 2:
        print('Empate!')
    else:
        print('Opção invalida!')