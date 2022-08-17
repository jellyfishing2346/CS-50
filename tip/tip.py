def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    dollar_sign = d.replace("$", " ")
    return float(dollar_sign)



def percent_to_float(p):
    # TODO
    percent = p.replace("%", " ")
    percent_convert = float(percent) / 100
    return percent_convert


main()