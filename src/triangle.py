import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a_side: int, b_side: int, c_side: int):
        self.name = 'Triangle'
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side
        self.check_if_can_create_triangle(a_side, b_side, c_side)

    def get_area(self) -> float:
        semi_perimeter = self.get_perimeter() / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.a_side) *
                         (semi_perimeter - self.b_side) * (semi_perimeter - self.c_side))
        return round(area, 2)

    def get_perimeter(self) -> float:
        return self.a_side + self.b_side + self.c_side

    @staticmethod
    def check_if_can_create_triangle(a_side: int, b_side: int, c_side: int):
        if not (a_side > 0 and b_side > 0 and c_side > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {a_side}, {b_side}, {c_side}')

        if not (a_side + b_side > c_side and a_side + c_side > b_side and c_side + b_side > a_side):
            raise ValueError(f'Unable to create a triangle with sides: {a_side}, {b_side}, {c_side}')
