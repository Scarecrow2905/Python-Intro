# Index operators [] = Gives access to a sequence's element (str, list, tuples)

name = "tommy håvåg!"

#if(name[0].islower()):
    #name = name.capitalize()

first_name = name[0:5].capitalize()
last_name = name[6:-1].upper()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)