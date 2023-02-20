
def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if 16 < idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPICIONAL.'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


nascimento = int(input('Em que ano voce nasceu? '))
print(voto(nascimento))