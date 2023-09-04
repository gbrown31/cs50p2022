# x = int(input(" what's x? "))
x = input(" what's x? ")
y = input(" what's y? ")

# z = int(x) + int(y)
z = float(x) + float(y)

z = round(z)

print(z)

# int formatting
print(f"{z:,}")

# floating point has upper bound, int does not have an upper bound

# rounding alternative
print(f"{z:.2f}")