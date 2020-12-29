#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def happy(cur):
            if cur == 1:
                return True
            if cur in seen:
                return False
            seen.add(cur)
            digits = [int(d) for d in str(cur)]
            return happy(sum(d*d for d in digits))

        return happy(n)


# @lc code=end
