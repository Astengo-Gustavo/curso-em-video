'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

n = int(input('Digite um número inteiro: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('É primo')
else:
    print('Não é primo')

