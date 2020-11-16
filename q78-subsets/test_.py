from solution import Solution

solve = Solution().subsets


def test_default():
    assert {frozenset(i) for i in solve([1, 2, 3])} == {
        frozenset(),
        frozenset([1]),
        frozenset([2]),
        frozenset([1, 2]),
        frozenset([3]),
        frozenset([1, 3]),
        frozenset([2, 3]),
        frozenset([1, 2, 3])}


def test_corner_cases():
    assert {frozenset(i) for i in solve([1])} == {
        frozenset(),
        frozenset([1])}
