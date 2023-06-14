import pytest
from src.triangle import Triangle


@pytest.mark.parametrize('a_side, b_side, c_side, expected_perimeter, expected_area',
                         [
                             (3, 5, 3, 11, 4.15),
                             (10, 12, 8, 30, 39.69)
                         ]
                         )
def test_triangle_creation_positive(a_side, b_side, c_side, expected_perimeter, expected_area):
    triangle = Triangle(a_side, b_side, c_side)
    assert triangle.name == 'Triangle', 'Expected name is Triangle'
    assert triangle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert triangle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('a_side, b_side, c_side',
                         [
                             (0, 5, 5),
                             (-1, 2, 3),
                             (3, 5, 2),
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                             'can not create rectangle with these sides'
                         ])
def test_triangle_creation_negative(a_side, b_side, c_side):
    with pytest.raises(ValueError):
        Triangle(a_side, b_side, c_side)


def test_two_triangle_areas_sum():
    expected_sum = 43.84
    triangle_1 = Triangle(3, 5, 3)
    triangle_2 = Triangle(10, 12, 8)
    assert triangle_1.add_area(triangle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_triangle_areas_sum_negative(some_other_class):
    triangle_1 = Triangle(10, 10, 10)
    with pytest.raises(ValueError):
        triangle_1.add_area(some_other_class)
