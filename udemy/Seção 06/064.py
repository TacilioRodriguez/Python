# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Desafio Hurdle 4


def vire_direita():
    turn_left()
    turn_left()
    turn_left()


def salto():
    turn_left()
    if front_is_clear() == True:
        move()
    elif wall_in_front == True:
        vire_direita()
    else:
        turn_left()


while not at_goal():
    if right_is_clear() != False:
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        salto()
    else:
        at_goal()


# Ou de forma mais clara colocando as informações em uma função

def jump():
    turn_left()
    while wall_on_right()
        move()

    turn_left()
    move()
    turn_right()

    while front_is_clear():
        move()

    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()