# Prompt the user to enter an expression
expression = input("Expression: ")

# Convert variables
x, y, z = expression.split()

# x and z are num1 and num2
num1 = double(x)
num2 = double(z)

if y == "+":
    result = num1 + num2
elif y == "-"
    result = num1 - num2
elif y == "*"
    result = num1 * num2
elif y == "/"
    result = num1 / num2
else:
    result = 0

