'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
print('Vamos jogar Par ou Impar!')
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Escolha um número: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! você venceu {v} vezes.')

