from solution import Solution

solve = Solution().maxSubArray


def test_default():
    assert solve([-2,1,-3,4,-1,2,1,-5,4]) == 6


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([0]) == 0
    assert solve([-2,1]) == 1

def test_nonegative_input():
    assert solve([-1]) == -1
    assert solve([-2147483647]) == -2147483647