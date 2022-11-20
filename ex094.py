galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = input('Nome: ')
    while True:
        pessoa['Sexo'] = input('Sexo: [M/F]').upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N} ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-=' * 30) # até a linha 22 é a leitura dos dados, da 23 em diante é a analise dos resultados
print(f'A) Ao    todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]} ',end='')
print()
print('D) Lista das pessoas que estão acima da média: ',end='')
for p in galera:
    if p['Idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')