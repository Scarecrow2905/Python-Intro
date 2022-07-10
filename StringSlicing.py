# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Tommy Håvåg"

first_name = name[0:5]
last_name = name[6:11]
funky_name = name[0:11:2] # [::1] You can leave them blank with only : and Python will assume it's the full length of the string
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# Website example

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
