#  the user enters a value and assigns the input to the variable
var = input("Please enter a value: ")

# 2a: Print the value of var as upper case
upper_Case = var.upper()
# capitalises user's input [var] using .upper() function

print(upper_Case)

# 2b: Print the number of characters in var
count = len(upper_Case)
# len(upper_case) counts the characters in the user's input

print(f"The number of characters in your sentence is {count}")
# f("  {[other data types]} ")
# concatenates data types and typecasts to str

# 2c: Does it contain numeric characters? isdecimal method
num_check = any(ltr.isdecimal() for ltr in upper_Case)

# ltr refers to letters in upper_Case
# ltr.isdecimal() a func that checks if any characters are numbers in upper_Case

if num_check is True:
    print("how'd those numbers get in there?")
else:
    print("wow alphabetti spaghetti")