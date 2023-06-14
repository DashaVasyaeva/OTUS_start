from src.figure import Figure


class Square(Figure):
    def __init__(self, a_side: int):
        self.name = 'Square'
        self.a_side = a_side
        self.check_if_can_create_square(a_side)

    def get_area(self) -> float:
        return self.a_side * self.a_side

    def get_perimeter(self) -> float:
        return 4 * self.a_side

    @staticmethod
    def check_if_can_create_square(a_side: int):
        if a_side <= 0:
            raise ValueError(f'Side must be greater than 0. Got: {a_side}')
