# Lists = used to store multiple items in a single variable

food = ["Pizza", "Taco", "Hamburger", "Ramen", "Spaghetti"]

food[0] = "Sushi"
# This will replace "Pizza"

#print(food[0])

food.append("Eggs") #This will append a new element to the list
food.remove("Sushi")
food.pop() # This will remove the last element
food.insert(3, "cake") # This will add an element at the given position
food.sort() # This will sort a list alphabetically
food.clear # This will clear the whole list, remove everything

for x in food:
    print(x)