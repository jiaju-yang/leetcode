from solution import Solution

solve = Solution().merge


def test_default():
    assert solve([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]]


def test_corner_cases():
    assert solve([[1, 4], [4, 5]]) == [[1, 5]]
    assert solve([]) == []


def test_nonsorted():
    assert solve([[1, 4], [0, 4]]) == [[0, 4]]
