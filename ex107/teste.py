import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'o dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentado 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p, 10)}')
