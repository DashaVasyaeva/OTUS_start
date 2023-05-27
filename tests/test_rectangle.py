import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize('a_side, b_side, expected_perimeter, expected_area',
                         [
                             (3, 5, 16, 15),
                             (10, 12, 44, 120)
                         ]
                         )
def test_rectangle_creation_positive(a_side, b_side, expected_perimeter, expected_area):
    rectangle = Rectangle(a_side, b_side)
    assert rectangle.name == 'Rectangle', 'Expected name is Triangle'
    assert rectangle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('a_side, b_side',
                         [
                             (0, 5),
                             (-1, 2),
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                         ])
def test_rectangle_creation_negative(a_side, b_side):
    with pytest.raises(ValueError):
        Rectangle(a_side, b_side)


def test_two_rectangle_areas_sum():
    expected_sum = 135
    rectangle_1 = Rectangle(3, 5)
    rectangle_2 = Rectangle(10, 12)
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_rectangle_areas_sum_negative(some_other_class):
    rectangle_1 = Rectangle(10, 10)
    with pytest.raises(ValueError):
        rectangle_1.add_area(some_other_class)
