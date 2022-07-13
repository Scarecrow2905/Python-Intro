# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
# Instead of doing all these we can simplify it to a single line of code like below:
#print(num)

round(abs(float(input("Enter a hole positive number: "))))

