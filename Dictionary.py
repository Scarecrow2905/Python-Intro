# Dictionary = #dictionary =  A changeable, unordered collection of unique key:value pairs
#                             Fast because they use hashing, allow us to access a value quickly

capitals = {"Norway": "Oslo",
            "India": "New Dehli",
            "USA": "Washington DC",
            "Russia": "Moscow",
            "England": "London"}

# A dictionary can be altered after the program is running, so we can add a new key and value.
capitals.update({"Germany": "Berlin"})
# You can also update existing key values by using .update
capitals.update({"USA": "Las Vegas"})
# We can also remove a key by using the .pop method
capitals.pop("Russia") # No curly brackets needed here
# We can also clear everything just as in lists and tuples
#capitals.clear()

#print(capitals["Norway"])   #This will print Oslo as Oslo is the key of Norway in this case
#print(capitals["Germany"])  # This wouldn't work as Germany doesn't exist in capitals, the program will stop

#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, value in capitals.items():
    print(key, value)
