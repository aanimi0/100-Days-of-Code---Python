from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])


user_dictionary = {"key": {"another_key":"another_value"}}

print(user_dictionary["key"]["another_key"])