'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''
tot = 0
tot1000 = 0
menor = 0
cont = 0
barato = ''
print('_' * 50)
print('{:-^40}'.format('Loja Super Baratão'))
print('_' * 50)
while True:
    produto = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o valor dp produto? R$'))
    cont += 1
    tot += preco
    if preco >= 1000:
        tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total da sua compre é R${tot:10.2f}')
print(f'houve um total de {tot1000} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA'))
