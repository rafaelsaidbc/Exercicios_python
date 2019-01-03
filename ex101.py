def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return print(f'Você tem {idade} anos. Ainda não vota!')
    elif 16 >= idade < 18 or idade >= 65:
        return print(f'Você tem {idade} anos. Voto opicional!')
    else:
        return print(f'Você tem {idade} anos. Voto obrigatório!')


voto(int(input('Em que ano você nasceu? ')))
