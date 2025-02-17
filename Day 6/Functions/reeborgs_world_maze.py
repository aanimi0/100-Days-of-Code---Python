def turn_right():
    turn_left()
    turn_left()
    turn_left()


def adjust_position():
    while wall_in_front():
        if right_is_clear():
            turn_right()
        else:
            turn_left()


# def move_around_pole():
#    turn_right()
#    move()
#    turn_right()
#    move()

def walk():
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()