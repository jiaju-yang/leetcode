from solution import Solution

solve = Solution().twoSum


def test_default():
    assert solve([2, 7, 11, 15], 9) == [1, 2]
    assert solve([2, 3, 4], 6) == [1, 3]


def test_corner_cases():
    assert solve([-1, 0], -1) == [1, 2]
