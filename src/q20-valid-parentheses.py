#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in self.brackets.values():
                stack.append(b)
            elif b in self.brackets:
                if not stack or stack.pop() != self.brackets[b]:
                    return False
            else:
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
