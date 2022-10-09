'''
crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dolares ela pode comprar
considere o valor da cotação do dia
'''

real = float(input(' qual valor você quer converter: R$ '))
dolar = real / 4.76

print('com R${:.2f} você pode convereter para US${:.2f}.'.format(real, dolar))