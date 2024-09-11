import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total_area = self.get_square() + other.get_square()
            # Find factors of total_area to create a new rectangle
            width = math.sqrt(total_area)
            height = total_area / width
            return Rectangle(width, height)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)) and n > 0:
            total_area = self.get_square() * n
            # Find factors of total_area to create a new rectangle
            width = math.sqrt(total_area)
            height = total_area / width
            return Rectangle(width, height)
        return NotImplemented

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

print(r1.get_square())
print(r2.get_square())

r3 = r1 + r2
print(round(r3.get_square(), 6))

r4 = r1 * 4
print(round(r4.get_square(), 6))

print(Rectangle(3, 6) == Rectangle(2, 9))
