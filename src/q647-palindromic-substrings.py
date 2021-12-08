#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.extend_substring(i, i, s)
            count += self.extend_substring(i, i+1, s)
        return count

    def extend_substring(self, start, end, s):
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            count += 1
            start -= 1
            end += 1
        return count


# @lc code=end
solve = Solution().countSubstrings


def test_default():
    assert solve('abc') == 3
    assert solve('abbc') == 5


def test_corner_cases():
    assert solve('aaa') == 6
    assert solve('a') == 1
    assert solve('aa') == 3
