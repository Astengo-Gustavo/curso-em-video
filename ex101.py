def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Você tem {idade} anos: NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos: OPCIONAL'
    else:
        return f'Você tem {idade} anos: OBRIGATORIO'


#programa principal
anonasc = int(input('em que ano você nasceu? '))
print(voto(anonasc))