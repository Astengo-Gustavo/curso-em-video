'''
Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #o usuário tenta advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você acertou, o número que eu pensei foi {}'.format(computador))
else:
    print('Você errou, o número que eu pensei foi {}!'.format(computador))

