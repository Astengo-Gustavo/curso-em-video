jogador = {}
partidas = []
jogador['Nome'] = input('Nome do jogador: ')
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols aa partida {c + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i + 1} fez {v} gols.')
print('-=' * 30)
print(f'Foi um total de {jogador["total"]} gols.')