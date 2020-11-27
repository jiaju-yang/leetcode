from solution import Solution

solve = Solution().kClosest


def test_default():
    assert {tuple(point) for point in solve([[1, 3], [-2, 2]], 1)} == {(-2, 2)}
    assert {tuple(point) for point in solve(
        [[3, 3], [5, -1], [-2, 4]], 2)} == {(3, 3), (-2, 4)}


def test_corner_cases():
    assert {tuple(point) for point in solve([[1, 3]], 1)} == {(1, 3)}
