def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # remove leading dollar sign
    d = d.replace("$", "")
    # convert string to float
    return float(d)


def percent_to_float(p):
    # remove trailing percentage sign
    p = p.replace("%", "")
    # convert string to float
    return float(p) / 100


main()