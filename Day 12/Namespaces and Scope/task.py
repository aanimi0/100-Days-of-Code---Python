enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope
def drink_potion():
    potion_strength = 2
    print()

drink_potion()
#print(potion_strength)
#global_scope
player_health = 10

