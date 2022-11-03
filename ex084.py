'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
pessoas = list()
dados = list()
mai = men = 0
while True:
    dados.append(input('nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Quer continnuar? [S/N]').strip()[0]
    if resp in 'Nn':
        break


print(pessoas)
print(f'você cadastrou {len(pessoas)} pessoas.')
print(f'o maior peso é de {mai}kg ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'o menor peso é de {men}kg ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')
