from solution import Solution

solve = Solution().maxArea


def test_default():
    assert solve([1,8,6,2,5,4,8,3,7]) == 49
    assert solve([4,3,2,1,4]) == 16


def test_corner_cases():
    assert solve([1]) == 0
    assert solve([]) == 0
    assert solve([1,1]) == 1
    assert solve([1,2,1]) == 2
