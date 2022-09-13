'''
Faça um programa que leia o sexo de uma pessoa.
Mas só aceite os valores 'M' e 'F'.
caso esteja errado, peça a digitação novamente até ter
um valor correto
'''
s = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]
while s not in 'MF':
    s = input('Dados invalidos, informe o seu sexo[M/F]: ').upper()
print('Seu genero é {}.'.format(s))
