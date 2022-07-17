import random

x = random.randint(1, 6)
y = random.random()

myList = ["Stein", "Saks", "Papir"]
z = random.choice(myList)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "Ace"]

random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)

