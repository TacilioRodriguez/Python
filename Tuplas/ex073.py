"""
Crie um tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados da tabela.
b) Os ultimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabetica
d) Em que posição na tabela esta o time da Chapeconense
"""

times = ('ATLÉTICO-MG', 'PALMEIRAS', 'FLAMENGO', 'FORTALEZA', 'BRAGANTINO', 'CORINTHIANS', 'INTERNACIONAL', 'FLUMINENSE', 'ATHLETICO-PR', 'CUIABÁ',
         'ATLÉTICO-GO', 'SÃO PAULO', 'CEARÁ', 'SANTOS', 'BAHIA', 'JUVENTUDE', 'AMÉRICA-MG', 'GRÊMIO', 'SPORT', 'CHAPECOENSE')

print(f'Os 5 primeiros colocados são ', times[0:5])
print(f'Os ultimos 4 times da tabela são', times[-5::])
print('Lista em Ordem Alfabetica', sorted(times))
print('A CHAPECOENSE esta na', times.index('CHAPECOENSE')+1,'ª Posição')