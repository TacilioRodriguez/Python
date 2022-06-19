def vire_direita():
    turn_left()
    turn_left()
    turn_left()

def salto():
    turn_left()
    move()
    vire_direita()
    move()
    vire_direita()
    move()
    turn_left()

cont = 0
while cont < 12:
    if front_is_clear() != False:
        move()
        cont +=1
    elif wall_in_front() == True:
        salto()
        cont +=1
    else:
        at_goal()

