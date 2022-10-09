'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros
        colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Corinthians.
'''

time = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo',
        'Corinthians', 'Atheltico PR', 'Atletico MG', 'America MG',
        'Goais', 'Botafogo', 'Santos', 'Bragantino', 'São Paulo',
        'Fortaleza', 'Ceara SC', 'Coritiba', 'Avai', 'Cuiaba',
        'Atlético GO', 'Juventude')
print(f'Lista de times: {time}')
print('-=' * 15)
print(f'os 5 primeiros times da tabela são: {time[0:5]}')
print('-=' * 15)
print(f'Os ultimos 4 da tabela são: {time[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(time)}')
print('-=' * 15)
print(f'O Corinthians está na {time.index("Corinthians")+1}º posição')
