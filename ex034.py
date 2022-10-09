'''
Escreva um programa que pergunte o salário de um funcionario e calcule o
valor do seu aumento. Para salários superiores a R$1250,00, calculeum aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%.
'''
salario = float(input('Qual o salário do funcionario? '))

if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)

print('O salário atual de {} com aumento será {}. '.format(salario,aumento))