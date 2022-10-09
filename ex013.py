'''
faça um algoritimo que leia o salario de
um funcionario e mostre seu novo salario
com 15% de aumento
'''
salario = float(input('qual é o salario de um funcionario? R$ '))
aumento = salario + (salario * 15 / 100)

print('um funcionario que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario,aumento))