# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruit_names = ["Apple", "Banana", "Pear", "Watermelon"]
for fruit in fruit_names:
   def fruits_append(fruit):
# TODO: Use a for loop to print each fruit in the list
    for fruit in fruit_names:
        print(fruit)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count >= 1:
   print(count)
   print-=1
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
squares = [i ** 2 for i in range(1, 11)]
for square in squares:
    print(square)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
#shuffle a list
colors = ["Red","Orange","Yellow","Green","Blue"]

# TODO: Use a for loop to select and print 3 random colors from the list
random.shuffle(colors)
print(colors, 3)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions


# TODO: Use a while loop to create a simple calculator

      