import random

# #import my_module
#
# random_integer = random.randint(1,10)
#
# print(random_integer)
# #print(my_module.my_favourite_number)
#
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
# random_float = random.uniform(1,10)
# #print(random_float)


headsortails_Generator = random.randint(0,1)

if headsortails_Generator == 0:
    print(f"Heads {headsortails_Generator}")
else:
    print(f"Tails {headsortails_Generator}")

