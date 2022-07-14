# function = a block of code which is executed only when it is called
# also known as invoking a function

def hello(name, name2, number): # Name is now a parameter, it has recieved an argument (str) which it can use within
    print("Hello "+name+".")
    print("Have a nice day, "+name2+"!")
    print("This is a number: "+ str(number)+".")

first_name = "Scarecrow"
second_name = "Paarl"
random_number = 23


hello(first_name, second_name, random_number) # This is an argument, you send information to the function which it can use.