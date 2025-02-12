import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
randomInt = random.randint(0,4)
indexedFriends = friends[randomInt]

#1
print(indexedFriends)

#2
print(random.choice(friends))
