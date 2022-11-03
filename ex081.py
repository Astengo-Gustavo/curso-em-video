'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []

while True:
    lista.append(int(input('digite um número: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
lista.sort(reverse = True)
print('=' * 30)
print(f'os numeros digitados em ordem decrescente foram {lista}')
print(f'Foram digitados {len(lista)} números')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não foi encontrado')
