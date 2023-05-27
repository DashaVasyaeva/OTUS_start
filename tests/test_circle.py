import pytest
from src.circle import Circle


@pytest.mark.parametrize('radius, expected_perimeter, expected_area',
                         [
                             (3, 18.85, 28.27),
                             (10, 62.83, 314.16)
                         ]
                         )
def test_circle_creation_positive(radius, expected_perimeter, expected_area):
    circle = Circle(radius)
    assert circle.name == 'Circle', 'Expected name is Circle'
    assert circle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert circle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('radius',
                         [
                             0, (-1)
                         ],
                         ids=[
                             'radius is zero',
                             'radius is negative',
                             ])
def test_circle_creation_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_two_circle_areas_sum():
    expected_sum = 342.43
    circle_1 = Circle(3)
    circle_2 = Circle(10)
    assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_circle_areas_sum_negative(some_other_class):
    circle_1 = Circle(10)
    with pytest.raises(ValueError):
        circle_1.add_area(some_other_class)
