#Logical operators (and,or,not) = used to check if two or more conditional statements are true.

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 20:
    print("This is fine!")
    print("No sweating to death!")
elif temp < 0 or temp > 25:
    print("It's bad today")
    print("AC time!")

if not(temp >= 0 and temp <= 20):
    print("It's bad today")
    print("AC time!")
elif not (temp < 0 or temp > 25):
    print("This is fine!")
    print("No sweating to death!")