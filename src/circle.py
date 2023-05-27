import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        self.name = 'Circle'
        self.radius = radius
        self.check_if_can_create_circle(radius)

    def get_area(self) -> float:
        return round(math.pi * (self.radius**2), 2)

    def get_perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 2)

    @staticmethod
    def check_if_can_create_circle(radius: int):
        if not (radius > 0):
            raise ValueError(f'Radius must be greater than 0. Got: {radius}')
