from solution import Solution

solve = Solution().permuteUnique


def test_default():
    assert {tuple(i) for i in solve([0, 1])} == {
        (1, 0),
        (0, 1)}
    assert {tuple(i) for i in solve([1, 2, 3])} == {
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 2, 1),
        (3, 1, 2)}

def test_duplicate():
    assert {tuple(i) for i in solve([1, 1, 2])} == {
        (1, 1, 2),
        (1, 2, 1),
        (2, 1, 1)}
    assert {tuple(i) for i in solve([1, 1, 2, 2])} == {
        (2, 1, 1, 2),
        (1, 2, 1, 2),
        (1, 1, 2, 2),
        (2, 1, 2, 1),
        (1, 2, 2, 1),
        (2, 2, 1, 1)}

def test_corner_cases():
    assert {tuple(i) for i in solve([1])} == {
        (1,)}
