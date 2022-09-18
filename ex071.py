'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai
informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('=' * 30)
print('{:^30}'.format('Banco'))
print('=' * 30)
valor = int(input('Qual valor deseja sacar? R$'))
total = valor
ced = 50
cedtot = 0
while True:
    if total >= ced:
        total -= ced
        cedtot += 1
    else:
        if cedtot > 0:
            print(f'Total de {cedtot} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            ced = 0
        cedtot = 0
        if ced == 0:
            break
print('=' * 30)
print('Volte sempre')
