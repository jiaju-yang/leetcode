from solution import Solution

solve = Solution().canPartition


def test_default():
    assert solve([1, 5, 11, 5]) == True
    assert solve([1, 2, 3, 5]) == False
    assert solve([3, 3, 3, 4, 5]) == True


def test_corner_cases():
    assert solve([1, 1]) == True
    assert solve([2, 0]) == False
    assert solve([1]) == False
