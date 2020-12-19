from solution import Solution

solve = Solution().twoSum


def test_default():
    assert solve([2, 7, 11, 15], 9) == [0, 1]
    assert solve([3, 2, 4], 6) == [1, 2]


def test_corner_cases():
    assert solve([3, 3], 6) == [0, 1]
    assert solve([1, 2], 3) == [0, 1]
