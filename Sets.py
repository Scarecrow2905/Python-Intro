# set = collection which is unordered, unindexed. No dublicate values

utensils = {"Fork", "Spoon", "Knife"}
dishes = {"Bowl", "Cup", "Plate", "Knife"}

#utensils.add("Napkin")
#utensils.remove("Spoon")
#utensils.clear()
#utensils.update(dishes) # This will add the set "dishes" to "utensils"
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes)) #This will show what utensils has that dishes don't
print(utensils.intersection(dishes)) #This will show what the two variables have in commmon

for x in dinner_table:
    print(x)