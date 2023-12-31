# create a class for rectangle
class Rectangle:
    # create a method for the rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def shape(self):
        if self.width >= 50 or self.height >= 50:
            return "The shape is too big."

        for i in range(self.height):
            print("*" * self.width)
        return f"Rectangle(width={self.width},height={self.height})"

# create a class for square
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def diagonal(self):
        return (self.side ** 2) ** 0.5

    def shape(self):
        if self.side >= 50:
            return "The shape is too big."

        for i in range(self.side):
            print("*" * self.side)
        return f"Square(side={self.side})"