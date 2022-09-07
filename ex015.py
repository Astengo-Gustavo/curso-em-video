'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia eR$0,15 por km rodado.
'''
dias = int(input('quantos dias o carro foi utilizado? '))
km = float(input('por quantos km percorreu? '))
total = (dias * 60) + (km * 0.15)

print('o total a pagar é de R${:.2f}'.format(total))