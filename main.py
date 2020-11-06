from calculator import Calculator

# calculations created as an instance of Calculator class
calculations = Calculator()

# executing add function and printing resulting value
print(calculations.add(4, 6))

# executing subtract function and printing resulting value
print(calculations.subtract(24, 13))

# executing multiply function and printing resulting value
print(calculations.multiply(7, 13))

# executing divide function and printing resulting value
print(calculations.divide(24, 6))

# executing divisible by function and printing resulting value
print(calculations.divisible_by(44, 11))

# executing function that calculates the area of a triangle and printing resulting value
print(calculations.area_of_triangle(12, 9))

# executing function that takes a measurement in inches and converts it to cm, and printing the value
print(calculations.inch_to_cm_converter(38))


