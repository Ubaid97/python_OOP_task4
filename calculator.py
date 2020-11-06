# This class contains the functions performing the arithmetic operations
class Calculator:

    # function add together the two numbers passed in by the user
    def add(self, num1, num2):
        return num1 + num2

    # function takes in two numbers and subtracts the second from the first
    def subtract(self, num1, num2):
        return num1 - num2

    # function takes in two numbers and multiplies them together
    def multiply(self, num1, num2):
        return num1 * num2

    # function takes two numbers and divides the first by the second
    def divide(self, num1, num2):
        return num1 / num2

    # function takes two numbers and checks whether the first is divisible by the second
    def divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    # function takes the height and base of a triangle (in any unit) and works out the area of the triangle
    def area_of_triangle(self, height, base):
        return (height * base) / 2

