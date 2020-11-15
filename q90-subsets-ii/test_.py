from solution import Solution

solve = Solution().subsetsWithDup


def test_default():
    result = solve([1, 2, 2])
    assert len(result) == 6
    assert {frozenset(i) for i in result} == {
        frozenset(),
        frozenset([1]),
        frozenset([2]),
        frozenset([1, 2]),
        frozenset([2, 2]),
        frozenset([1, 2, 2])}

    result = solve([5, 5, 5, 5, 5])
    assert len(result) == 6
    assert {frozenset(i) for i in result} == {
        frozenset(),
        frozenset([5]),
        frozenset([5, 5]),
        frozenset([5, 5, 5]),
        frozenset([5, 5, 5, 5]),
        frozenset([5, 5, 5, 5, 5])}


def test_corner_cases():
    assert {frozenset(i) for i in solve([1])} == {
        frozenset(),
        frozenset([1])}
