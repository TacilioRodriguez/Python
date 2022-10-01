# Verificar se um número é primo

def check_num_primo(numero):
    primo = True
    for i in range(2, numero):
        if (numero % i) == 0:
            primo = False
    if primo:
       print('É um numero Primo')
    else:
        print('Não é um numero Primo')


number = int(input("Digite um Numero Inteiro: "))
check_num_primo(numero=number)