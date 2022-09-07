'''
faça um programa que leia a largura e a altura
de uma parede em metros, calcule  a sua area e a quantidade
de tinta nescessaria para pinta-la, sabendo que cada litro de tinta
pinta uma area de 2m².
'''

largura = float(input('qual a largura? '))
altura = float(input('qual a altura? '))
area = largura * altura
tinta = area / 2

print('sua parede tem a dimensão de  {} x {} e sua area é de {}m².'.format(largura,altura,area))
print('para pintar essa parede, você precisará {} L de tinta.'.format(tinta))

