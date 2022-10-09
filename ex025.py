'''
Crie um programa que leia o nome de uma pessoa
e diga se ela tem 'Silva' no nome.
'''
nome = input('Digite seu nome: ').strip()
#print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))

if 'Silva' in nome:
    print('Seu nome tem silva? Sim')
else:
    print('Seu nome tem silva? não')