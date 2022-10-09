'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
computador = randint(0,10)
print('Vou pensar em um número entre 0 e 10.tente advinhar...')
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input('Em que número eu pensei: '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('é mais..., tente mais uma vez.')
        elif jogador > computador:
            print('Menos..., tente mais uma vez.')
print('Você acertou com {} tentativas, Parabens!'.format(tentativa))