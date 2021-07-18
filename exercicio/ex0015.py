#Calular o valor a ser pago por um carro alugado de acordo com o valor de dias digitado

km = float(input('Qual o KM percorrido? KM '))
dia = int(input('Por quantos dias ele foi alugado? '))
vl = (dia*60) + (km*0.15)
print('O km total é de {:.2f}, por {} dias. O valor total a ser pago é de R${:.2f}'.format(km,dia,vl))