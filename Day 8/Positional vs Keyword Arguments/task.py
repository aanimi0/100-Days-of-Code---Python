# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
#
# #function with more than 1 input
# def greet_with(name,location):
#     print(f"How are you {name} ?")
#     print(f"How is the weather in {location}?")
#
# greet_with(location ="resita",name="alex")

def calculate_love_score(name1, name2):
    word1 = "TRUE"
    word2 = "LOVE"

    name1 = name1.upper()
    name2 = name2.upper()

    word1_list = []
    word2_list = []

    for letter in name1:
        word1_list += letter

    for letter in name2:
        word2_list += letter

    attribute_list_1 = []
    totalPoints1 = 0

    for attribute in word1:
        if attribute not in attribute_list_1:
            attribute_value_1 = word1_list.count(attribute)
            totalPoints1 += attribute_value_1
            attribute_list_1.append(attribute)
            # print(f"Letter {attribute} occurs {attribute_value_1}")

    # print(f"Total= {totalPoints1}")

    attribute_list_2 = []
    totalPoints2 = 0

    for attribute in word2:
        if attribute not in attribute_list_2:
            attribute_list_2.append(attribute)
            attribute_value_2 = word2_list.count(attribute)
            totalPoints2 += attribute_value_2
            # print(f"Letter {attribute} occurs {attribute_value_2}")

    # print(f"Total = {totalPoints2}")
    # total = totalPoints1  totalPoints2

    score = int((str(totalPoints1) + str(totalPoints2)))
    print(score)

calculate_love_score("Kanye West", "Kim Kardashian")