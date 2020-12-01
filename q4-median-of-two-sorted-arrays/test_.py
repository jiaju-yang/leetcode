from solution import Solution

solve = Solution().findMedianSortedArrays


def test_default():
    assert solve([1, 3], [2]) == 2
    assert solve([1, 2], [3, 4]) == 2.5
    assert solve([1, 2, 3, 4, 5], [6]) == 3.5


def test_corner_cases():
    assert solve([0, 0], [0, 0]) == 0
    assert solve([], [1]) == 1
    assert solve([2], []) == 2
