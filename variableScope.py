# scope = The region that a variable is recognized
#          A variable is only available from inside the region it is created.
#          A global and locally scoped versions of a variable can be created.

name = "Tommy" # Global scope (available inside and outside functions)

def display_name():
    name = "Etternavn" # Local scope (available only inside this function)
    print(name)

display_name()
print(name)

# Python will prioritize variables as followed down below:
# L = Local
# E = Enclosed
# G = Global
# B = Built-in