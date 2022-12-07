def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
nome1 = input('digite um nome: ')
nome2 = input('Digite outro nome: ')
escreva(nome1)
escreva(nome2)