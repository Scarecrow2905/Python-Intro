# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Tommy", 29, "Male")

print(student.count("Tommy")) # Counts how many of "Tommy"'s there are
print(student.index("Male")) # Finds the Index/Position of the given element

for x in student:
    print(x)

if "Tommy" in student:
    print("Tommy is here")
