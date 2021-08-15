""" A confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Senior
- Acima: Master
"""
import datetime
nasc = int(input('Digite o ano de nascimento: '))
data = datetime.datetime.today()
categoria = data.year - nasc
if categoria <= 9:
    print('Mirim')
elif categoria > 9 and categoria <= 14:
    print('Infantil')
elif categoria > 14 and categoria <= 19:
    print('Junior')
elif categoria > 19 and categoria <= 20:
    print('Senior')
else:
    print('Master')
