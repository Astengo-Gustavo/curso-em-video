'''
Escreva um programa que leia um número inteiro qualquer
e peça para o úsuario escolher qual será a base de colnversão:
1 para binario
2 para octal
3 para hexadecimal
'''
num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINáRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convetido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opçãol invalida, tente novamente')
