from solution import Solution

solve = Solution().removeElement


def test_default():
    nums = [3, 2, 2, 3]
    assert solve(nums, 3) == 2
    assert nums == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert solve(nums, 2) == 5
    assert nums == [0, 1, 4, 0, 3]


def test_corner_cases():
    nums = [1]
    assert solve(nums, 2) == 1
    assert nums == [1]

    nums = []
    assert solve(nums, 2) == 0
    assert nums == []

    nums = [1]
    assert solve(nums, 1) == 0
    assert nums == []
