time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols aa partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N]').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar os dados de qual jogador ? [999 para parar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!Não existe jogador com codigo {busca}!')
    else:
        print(f' __ LEVATAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')