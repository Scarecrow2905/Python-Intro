# while loop = a statement that will execute its block of code
#              as long as its condition remains true

#name = ""
name = None
#while len(name) == 0:
while not name:
    name = input("Enter your name: ")

print("Hello "+name)