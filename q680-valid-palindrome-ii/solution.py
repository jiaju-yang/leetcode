#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                del_left, del_right = s[left+1:right+1], s[left:right]
                return del_left == del_left[::-1] or del_right == del_right[::-1]
            left += 1
            right -= 1
        return True

# @lc code=end
