#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    brackets = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in self.brackets:
                stack.append(self.brackets[b])
            elif not stack or stack.pop() != b:
                return False
        return not stack


# @lc code=end
solve = Solution().isValid


def test_default():
    assert solve('()')
    assert solve('()[]{}')
    assert not solve('(]')
    assert not solve('([)]')
    assert solve('{[]}')


def test_corner_cases():
    assert solve('')
    assert not solve('(')
    assert not solve('}')
    assert not solve('1')
