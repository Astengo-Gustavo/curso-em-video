'''
faça um algoritimo que leia o preço
de um produto e mostre seu novo preço
com 5% de desconto 
'''

preco = float(input('qual é o preço do produto: R$ '))
novo_preco = preco - (preco * 5 / 100)

print('seu produto custa R${:.2f}\ndesconto de R${:.2f}\nvalor total R${:.2f}'.format(preco,preco * 5 / 100,novo_preco))