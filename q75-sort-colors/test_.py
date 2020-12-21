from solution import Solution

solve = Solution().sortColors


def test_default():
    nums = [2, 0, 2, 1, 1, 0]
    solve(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    solve(nums)
    assert nums == [0, 1, 2]

    nums = [1, 2, 0]
    solve(nums)
    assert nums == [0, 1, 2]


def test_corner_cases():
    nums = [0]
    solve(nums)
    assert nums == [0]

    nums = [1]
    solve(nums)
    assert nums == [1]

    nums = [1, 0]
    solve(nums)
    assert nums == [0, 1]
