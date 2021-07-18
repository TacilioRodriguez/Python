
print('========= Programa -- Notas dos Alunos =========')
s = 0
for c in range(0, 5):
    n = int(input('Digite a nota:'))
    s = (s+n)
m = s/n
print('A somatoria das notas da Classe é {}, e a Média {}'.format(s,m))
print('FIM')