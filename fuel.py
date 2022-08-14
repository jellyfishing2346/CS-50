# Design a forever loop
while True:
    fraction = input("Fraction: ")
    try:
        # Attempting to split the fuel
        numerator, denominator = fraction.split("/")
        # Convert the fractions into integers
        newNum = int(numerator)
        newDen = int(denominator)
        # Calculate the fraction's percentage
        percentage = newNum / newDen
        # Checking if the fraction is less than 1, otherwise end the forever loop
        if percentage <  1:
            break
    except (ValueError, ZeroDivisionError):
            pass
# Make sure to multiply the fraction's percentage by 100
product = int (percentage * 100)
# Print E, if the fraction's percentage is less than 1
if product <= 1:
    print("E")
# Print F, if the fraction's precentage is greater than 99
elif product >= 99:
    print("F")
# Otherwise print % as the default statement
else:
    print(f"{product}%")