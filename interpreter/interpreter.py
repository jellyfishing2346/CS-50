# Prompt the user to enter an expression
expression = input("Expression: ")

# Convert variables
x, y, z = expression.split(" ")

# x and z are num1 and num2
num1 = float(x)
num2 = float(z)

# If y = +, then add the two integers
if y == "+":
    answer = num1 + num2
    print(answer)

# If y = -, then subtract the two integers
elif y == "-":
    answer = num1 - num2
    print(answer)

# If y = *, then multiply the two integers
elif y == "*":
    answer = num1 * num2
    print(answer)

# If y = /, then divide the two integers
elif y == "/":
    answer = num1 / num2
    print(answer)

# Display the answer
else:
    answer = " "
    print(answer)

