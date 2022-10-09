'''
Crie um programa que leia onome completo
de uma pessoa e mostre:
O nome com todas as letras maisculas
O nome com todas as letras minuscula
Quantas letras ao todo (sem os condiserar os espaços)
Quantas letras tem o primeiro nome
'''

nome = input('qual seu nome? ').strip()
print(nome.upper())
print(nome.lower())
print('Seu nome contem {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

