'''
Desenvolva um programa que pergunte a distancia de uma viagem
em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para
viagens até 200km e R$0,45 para viagens mais longas
'''
distancia = float(input('qual a distancia da sua viagem? '))

print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('o preço da da passagem é R${}.'.format(preco))
