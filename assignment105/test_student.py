
from a03 import saddle_points


def test_saddle_point():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert(saddle_points(matrix))==set([(0, 2)])

def test_no_saddle_points():
    assert(saddle_points([]))==set()

def test_none_saddle_points():
    matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    assert(saddle_points(matrix))==set()

def test_multiple_saddle_points_in_column():
    matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
    expected = set([(0, 1), (1, 1), (2, 1)])
    assert(saddle_points(matrix))== expected

def test_multiple_saddle_points_in_row():
    matrix = [[6, 7, 8], [5, 5, 5], [7, 5, 6]]
    expected = set([(1, 0), (1, 1), (1, 2)])
    assert(saddle_points(matrix))== expected

def test__saddle_point_inbetween():
    matrix = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]
    expected = set([(2, 2)])
    assert(saddle_points(matrix))==expected


if __name__ == '__main__':
    main()
