#Desenvolva um programa que pergunte a distancia de uma viagem em KM. 
#Calcule o preço da passagem, cobrando 0,50 por km para viagens de até 200km, e 0,45 para viagens mais longas

distancia = int(input('Digite a distancia em KM: '))
if distancia <=200:
    print("O valor da passagem é R${:.2f} reais".format(distancia*0.50))
else:
    print("O valor da passagem é R${:.2f} reais".format(distancia*0.45))
