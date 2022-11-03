lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('quer continuar? [S/N]').strip().upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista dos números pares é {par}')
print(f'A lista dos números impares é {impar}')