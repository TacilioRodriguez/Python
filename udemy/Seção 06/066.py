def vire_direita():
    turn_left()
    turn_left()
    turn_left()


def salto():
    move()
    turn_left()
    move()
    vire_direita()
    move()
    vire_direita()
    move()
    turn_left()


cont = 0
# for step in range(1, 11):
#    step = passo()
while cont < 6:
    salto()
    cont += 1