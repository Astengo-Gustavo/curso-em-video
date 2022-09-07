'''
Faça um programa que leia o ano de mascimento de um jovem
e informe, de acordo com sua idade:

se ele ainda vai se alistar ao serviço militar.
se é a hora de alistar.
Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
'''

from datetime import date
atual = date.today().year
genero = int(input('Qual seu genero, digite 1 para masculino ou 2 para feminino: '))
if genero == 2:
    print('Alistamento não obrigatorio')
    exit()
nasc = int(input('qual o seu ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))

if idade == 18:
    print('Você tem que se alistar!')
elif idade > 18:
    saldo = idade - 18
    print('Já passou {} anos do tempo do alistamento'.format(saldo))
    ano = atual - saldo
    print('Você deveria ter se alistado em {}.'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
