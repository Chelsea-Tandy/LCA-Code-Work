# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ("Apple", "Banana", "Watermelon")
for fruit in fruits:
    print(fruit)
# TODO: Add a fruit to the end of the list
fruits = ["Apple", "Banana", "Watermelon"]
fruits.extend(["Strawberry"])
print(fruits)
# TODO: Insert a fruit at the beginning of the list
fruits = ["Apple", "Banana", "Watermelon"]
fruits.insert(0, "Mango")
print(fruits)
# TODO: Remove a fruit from the list
fruitss = ["Apple", "Banana", "Watermelon"]
fruits.remove("Banana")
print(fruits)
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = (1, 2, 3, 4, 5)
print(numbers)
# TODO: Create a new list with each number squared
squared_numbers = [i ** 2  for i in range(1, 6)]
print(squared_numbers)
# TODO: Find the sum and average of the original numbers
total = 0
for i in range(1,6):
    total += i
average = total/5

# TODO: Print the results
print("Sum:",average)
print("Average:",average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_capitals = {
    "Argintina":"Buenos Aires",
    "Australia": "Canberra",
    "China": "Beijing",
    "Japan": "Tokyo"
    }
# TODO: Add a new country-capital pair
countries_capitals["Chile"]  = "Santiago"
# TODO: Update the capital of an existing country
countries_capitals["Australia"] = "Melbourne"
# TODO: Remove a country-capital pair
del countries_capitals["Argintina": "Buenos Aires"]
# TODO: Print the modified dictionary
print(countries_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Grape": "Green",
    "Peach": "Orange"
}
# TODO: Print all the fruits (keys)
for fruit in fruit_colors.keys():
    print(fruit)
# TODO: Print all the colors (values)
for color in fruit_colors.values():
    print(color)
# TODO: Print each fruit and its color
for fruit, color in fruit_colors.items():
    print(f"{fruit}:{color}")
# TODO: Check if a fruit is in the dictionary and print its color
fruit_colors = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Grape": "Green",
    "Peach": "Orange"
}

fruit = "Apple"
if fruit in fruit_colors:
    print(f"{fruit}'s color is {fruit_colors[fruit]}")
else:
    print(f"{fruit}not found")