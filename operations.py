#  the user enters a value and assigns the input to the variable
var = input("Please enter a value: ")

# the value of var is converted to uppercase using the upper() method
print("The value of var in upper case:", var.upper())

# Initialise a variable "count" which counts the characters in the string
count = 0

# this is a loop that iterates through every character in the string var
for char in var:
    # the count increases by 1 for each character. After the loop completes, count holds the total number of
    # characters in the string var.
    count += 1

# print the number of characters in var
print("The number of characters in var:", count)

# Check if var contains numeric characters using isdecimal method on the input string var to check if it contains
# only decimal characters (0 through 9). ask victoria because its not working
contains_number = var.isdecimal()
print(" Does var contain numeric characters?", contains_number)