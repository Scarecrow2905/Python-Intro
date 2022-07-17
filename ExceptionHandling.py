# Exception handling = Events detected during execution that interrupts the flow of the program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero, jackass!")
except ValueError as e:
    print(e)
    print("Only numbers please.")
except Exception as e:
    print(e)
    print("Something else went wrong") #This is considered better practice to have other errors
    # - Be handled first.
else:
    print(result)
finally:
    print("This will always execute.")

# This is considered bad practice, we don't want one exception to handle all errors
#except Exception:
    #print("Something went wrong!")