'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' PILULU Confecções '))
valor = float(input('Preço das compras: R$ '))
print(''' Formas de pagamento
 [1] à vista dinheiro/cheque
 [2] à vista no cartão 
 [3] 2x no cartão 
 [4] 3x ou mais no cartão''')
opcao = int(input('qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de  R${:.2f} sem juros'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcela em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
    total = valor
    print('Opção invalida, tente novamente')
print('Sua compra de R${:.2f}, vai custar R${:.2f}.'.format(valor, total))

