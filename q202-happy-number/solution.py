#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class SetSolution:
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


class TwoPointersSolution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.next(slow)
            fast = self.next(self.next(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False

    def next(self, n):
        return sum(int(d)*int(d) for d in str(n))


Solution = TwoPointersSolution
# @lc code=end
