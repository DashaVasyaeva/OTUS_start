import pytest
from src.square import Square


@pytest.mark.parametrize('a_side, expected_perimeter, expected_area',
                         [
                             (3, 12, 9),
                             (10, 40, 100)
                         ]
                         )
def test_square_creation_positive(a_side, expected_perimeter, expected_area):
    square = Square(a_side)
    assert square.name == 'Square', 'Expected name is Square'
    assert square.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert square.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('a_side',
                         [
                             0, (-1)
                         ],
                         ids=[
                             'side is zero',
                             'side is negative',
                             ])
def test_square_creation_negative(a_side):
    with pytest.raises(ValueError):
        Square(a_side)


def test_two_square_areas_sum():
    expected_sum = 109
    square_1 = Square(3)
    square_2 = Square(10)
    assert square_1.add_area(square_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_square_areas_sum_negative(some_other_class):
    square_1 = Square(10)
    with pytest.raises(ValueError):
        square_1.add_area(some_other_class)
