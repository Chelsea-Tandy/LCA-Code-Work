# Question 1: Arithmetic and Assignment Operators
x=2
y=3
# TODO: Add 3 to x using the += operator
x +=3
# TODO: Multiply y by 2 using the *= operator
y*2 
# TODO: Divide x by y and store the result in a variable called 'result'
result=y / x 
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a=30
b=10
c=5
# TODO: create a condition that checks is a is greater than b
a_greater_than_b = a > b
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b_is_even = b % 2 == 0
# TODO: Create a condition that checks if c is less than or equal to a
c_less_or_equal_to_a = c >= a
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

# TODO: Print the value of 'final_condition'
print = ("final result of the condition")
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = (int(input("Enter your test score (0-100): ")))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score > 60:
    grade = "D"
else:
    grade = "F"
# TODO: Print the grade for the given score
print=("the grade of the score" + grade)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter the thirst number: "))
num2 = float(input("Enter the second number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter operation('+','-',",'/')
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation :
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
else:print("Error: Division by zero!")
result = None
# TODO: Handle the case of division by zero
print("Invalid option!")
result = None
# TODO: Print the result of the operation
if result is not None:
    print("Result:, result")