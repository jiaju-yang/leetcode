from solution import Solution

solve = Solution().subsets


def test_default():
    result = solve([1, 2, 3])
    assert len(result) == 8
    assert {frozenset(i) for i in result} == {
        frozenset(),
        frozenset([1]),
        frozenset([2]),
        frozenset([1, 2]),
        frozenset([3]),
        frozenset([1, 3]),
        frozenset([2, 3]),
        frozenset([1, 2, 3])}


def test_corner_cases():
    result = solve([1])
    assert len(result) == 2
    assert {frozenset(i) for i in result} == {
        frozenset(),
        frozenset([1])}
