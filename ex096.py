def area(lar, comp):
    a = lar * comp
    print(f'A área de um terreno {lar}x{comp} é de {a}m².')


# programa principal
print('  Controle de terrenos  ')
print('-' * 30)
l = float(input('Largura ((m): '))
c = float(input('Comprimento (m): '))
area(l, c)