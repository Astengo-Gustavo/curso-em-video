'''
faça um programa que leia um angulo qualquer
e mostre na tela o valor do seno, cosseno
e tangente de desse angulo
'''
from math import radians, sin, cos, tan
an = float(input('digite o angulo que você deseja: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print('o ângulo de {}º tem o SENO de {:.2f}'.format(an, seno))
print('o ângulo de {}º tem o COSSENO de {:.2f}'.format(an, cosseno))
print('o ângulo de {}º tem a TANGENTE de {:.2f}'.format(an, tangente))



