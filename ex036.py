'''
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode execeder 30%
do salário, então o empréstimo será negado.
'''
valor_casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o valor do seu salario: R$ '))
ano = int(input('Em quantos anos de financiamento: '))

prestacao = valor_casa / (ano * 12)
limite = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa,ano), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))

if prestacao > limite:
    print('emprestimo negado')
else:
    print('emprestimo aprovado')
