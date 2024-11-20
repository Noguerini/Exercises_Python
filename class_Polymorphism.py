from abc import ABC, abstractmethod


class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        

class Square(Shape):
    pass

class Triangle(Shape):
    pass

shapes = [Circle(), Square(), Triangle()]