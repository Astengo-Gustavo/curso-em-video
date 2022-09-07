'''
Faça um programa que leia o coprimento
do cateto oposto w so cateto adjacente de um triangulo retangulo
calcule e mostre o comprimento da hipotenusa
'''
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)                                 # hi = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(hi))