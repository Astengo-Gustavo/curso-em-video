'''
crie um algoritimo que leia um numero
e mostre o seu dobro, o seu triplo e a raiz quadrada
'''

n = int(input('digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('o dobro de {} vale {}.\no triplo de {} vale {}.\na raiz quadrada de {} é igual a {}.'.format(n,d,n,t,n,r))