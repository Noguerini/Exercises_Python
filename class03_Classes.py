class Shape:
    def __init__(self, color, isFilled):
        self.color = color
        self.isFilled = isFilled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.isFilled == True else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, isFilled, radius):
        super().__init__(color, isFilled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius} cm^2") #Method overwriting
        super().describe()

class Square(Shape):
    def __init__(self, color, isFilled, width):
        super().__init__(color, isFilled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, isFilled, width, height):
        super().__init__(color, isFilled)
        self.width = width
        self.height = height

circle = Circle("red", True, 30)
circle.describe()