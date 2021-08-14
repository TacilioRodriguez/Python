#escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7 por cada km acima do limite

v = int(input("Digite a velocidade do Carro: "))
l = 80
if v >l:
    print("Você foi multado em R${:.2f} reais".format((v-l)*7))
else:
    print("Velocidade Ok!")