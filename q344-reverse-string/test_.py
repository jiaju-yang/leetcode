from solution import Solution

solve = Solution().reverseString


def test_default():
    s = ['h','e','l','l','o']
    solve(s)
    assert s == ['o','l','l','e','h']

    s = ['H','a','n','n','a','h']
    solve(s)
    assert s == ['h','a','n','n','a','H']


def test_corner_cases():
    s = ['h','e']
    solve(s)
    assert s == ['e','h']

    s = []
    solve(s)
    assert s == []

    s = ['h']
    solve(s)
    assert s == ['h']
