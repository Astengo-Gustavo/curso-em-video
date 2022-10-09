'''
crie um programa que leia um número real qualquer
pelo teclado e mostre na tela a sua porção inteira.
EX Digite um número: 6.127
o número 6.127 tem a parte inteira 6
'''
from math import trunc
num = float(input('digite um valor: '))
print('o valor digitado é {} e a sua porção inteira é {}'.format(num, trunc(num)))