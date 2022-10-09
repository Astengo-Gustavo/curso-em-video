'''
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar 
    [2] multiplicar 
    [3] maior 
    [4] novos números 
    [5] sair do programa''')
    opcao = int(input('qual é sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('a soma entre {} + {} é {}.'.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print('o resultado entre {} X {} é {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior valor é {}'.format(n1,n2, maior))
    elif opcao == 4:
        print('informe os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente!')
    sleep(2)
print('Fim do programa!')
