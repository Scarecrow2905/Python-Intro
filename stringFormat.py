# String format = Optional method that gives users
#                 more control when displaying output

#animal = "Cow"
#item = "Moon"

#print("The " + animal + " went over the " + item)
#print("The {} went over the {}".format(animal, item))
#print("The {0} went over the {1}".format(item, animal)) # Positional argument
#print("The {animal} went over the {item}".format(item="Moon", animal="Cow")) # keyword argument

#text = "The {} went over the {}"
#print(text.format(animal, item))

name = "Tommy"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) #The {:10} will allocate the number of spaces given within
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))


number = 1000

print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))