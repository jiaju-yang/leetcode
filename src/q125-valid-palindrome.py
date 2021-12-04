#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure = [c.lower() for c in s if c.isalpha() or c.isnumeric()]
        left, right = 0, len(pure) - 1
        while left < right:
            if pure[left] != pure[right]:
                return False
            left += 1
            right -= 1
        return True


# @lc code=end
solve = Solution().isPalindrome


def test_default():
    assert solve('A man, a plan, a canal: Panama')
    assert not solve('race a car')
    assert not solve('0P')


def test_corner_cases():
    assert solve('')
    assert solve(' ')
    assert solve(' a')
    assert not solve(' a b')
