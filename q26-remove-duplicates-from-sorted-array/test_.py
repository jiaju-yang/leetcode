from solution import Solution

solve = Solution().removeDuplicates


def test_default():
    nums = [1,1,2]
    assert solve(nums) == 2
    assert nums == [1, 2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    assert solve(nums) == 5
    assert nums == [0,1,2,3,4]


def test_not_modified():
    nums = [0,1,2]
    assert solve(nums) == 3
    assert nums == [0,1,2]


def test_corner_cases():
    nums = [0]
    assert solve(nums) == 1
    assert nums == [0]

    nums = []
    assert solve(nums) == 0
    assert nums == []
