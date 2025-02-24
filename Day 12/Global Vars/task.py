# Modifying Global Scope

enemies = 1


def increase_enemies(enemies):
    #global enemies should be avoided unless really necessary
    print(f"enemies inside function: {enemies}")
    return enemies + 1

new_enemy = increase_enemies(enemies)
print(f"enemies outside function: {new_enemy}")


def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(71))